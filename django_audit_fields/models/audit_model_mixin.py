import socket
from datetime import datetime
from typing import Tuple
from zoneinfo import ZoneInfo

from django.apps import apps as django_apps
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_revision.model_mixins import RevisionModelMixin

from ..constants import AUDIT_MODEL_UPDATE_FIELDS
from ..fields import HostnameModificationField, UserField


def utcnow() -> datetime:
    return datetime.now().astimezone(ZoneInfo("UTC"))


def update_device_fields(instance: "AuditModelMixin") -> Tuple[str, str]:
    device_id = getattr(settings, "DEVICE_ID", None)
    try:
        app_config = django_apps.get_app_config("edc_device")
    except LookupError:
        pass
    else:
        device_id = device_id or app_config.device_id

    if not instance.id:
        device_created = device_id or "00"
    else:
        device_created = instance.device_created
    device_modified = device_id or "00"
    return device_created, device_modified


class AuditModelMixin(RevisionModelMixin, models.Model):

    """Base model class for all models. Adds created and modified
    values for user, date and hostname (computer).
    """

    get_latest_by = "modified"

    created = models.DateTimeField(blank=True, default=utcnow)

    modified = models.DateTimeField(blank=True, default=utcnow)

    user_created = UserField(
        verbose_name=_("user created"),
        max_length=50,
        blank=True,
        help_text=_("Updated by admin.save_model"),
    )

    user_modified = UserField(
        verbose_name=_("user modified"),
        max_length=50,
        blank=True,
        help_text=_("Updated by admin.save_model"),
    )

    hostname_created = models.CharField(
        verbose_name=_("Hostname created"),
        max_length=60,
        blank=True,
        default=socket.gethostname,
        help_text="System field. (modified on create only)",
    )

    hostname_modified = HostnameModificationField(
        verbose_name=_("Hostname modified"),
        max_length=50,
        blank=True,
        help_text="System field. (modified on every save)",
    )

    device_created = models.CharField(
        verbose_name=_("Device created"), max_length=10, blank=True
    )

    device_modified = models.CharField(
        verbose_name=_("Device modified"), max_length=10, blank=True
    )

    locale_created = models.CharField(
        verbose_name=_("Locale created"),
        max_length=10,
        null=True,
        blank=True,
        help_text="Auto-updated by Modeladmin",
    )

    locale_modified = models.CharField(
        verbose_name=_("Locale modified"),
        max_length=10,
        null=True,
        blank=True,
        help_text="Auto-updated by Modeladmin",
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        try:
            # don't allow update_fields to bypass these audit fields
            update_fields = kwargs.get("update_fields", None) + AUDIT_MODEL_UPDATE_FIELDS
        except TypeError:
            pass
        else:
            kwargs.update({"update_fields": update_fields})
        dte_modified = utcnow()
        if not self.id:
            self.created = dte_modified
            self.hostname_created = self.hostname_created[:60]
        self.modified = dte_modified
        self.hostname_modified = self.hostname_modified[:50]

        self.device_created, self.device_modified = update_device_fields(self)

        super().save(*args, **kwargs)

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["-modified", "-created"]),
            models.Index(fields=["user_modified", "user_created"]),
        ]
