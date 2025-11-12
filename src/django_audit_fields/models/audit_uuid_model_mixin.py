from django.db import models
from django.utils.translation import gettext_lazy as _

from ..fields import UUIDAutoField
from .audit_model_mixin import AuditModelMixin

__all__ = ["AuditUuidModelMixin"]


class AuditUuidModelMixin(AuditModelMixin, models.Model):
    """Base model class for all models using a UUID and not
    an INT for the primary key.
    """

    id = UUIDAutoField(
        blank=True,  # ignored when editable=False, but if removed will trigger migrations
        editable=False,
        help_text=_("System auto field. UUID primary key."),
        primary_key=True,
    )

    class Meta(AuditModelMixin.Meta):
        abstract = True
        indexes = AuditModelMixin.Meta.indexes
