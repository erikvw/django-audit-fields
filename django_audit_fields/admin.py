from __future__ import annotations

from django.utils.translation import get_language_from_request
from django.utils.translation import gettext_lazy as _
from edc_utils import get_utcnow

from .constants import AUDIT_MODEL_FIELDS

audit_fields: tuple[str, ...] = tuple(AUDIT_MODEL_FIELDS)

audit_fieldset_tuple: tuple[str, dict[str, tuple[str, ...]]] = (
    _("Audit"),
    {"classes": ("collapse",), "fields": AUDIT_MODEL_FIELDS},
)


class ModelAdminAuditFieldsMixin:
    include_audit_fields_in_list_display: bool = True

    def save_model(self, request, obj, form, change) -> None:
        """Update audit fields from request object before save."""
        if not change:
            obj.user_created = request.user.username
            obj.created = get_utcnow()
            obj.locale_created = get_language_from_request(request, check_path=True)
        else:
            obj.user_modified = request.user.username
            obj.modified = get_utcnow()
            obj.locale_modified = get_language_from_request(request, check_path=True)
        super().save_model(request, obj, form, change)

    def get_list_display(self, request) -> tuple[str, ...]:
        list_display = super().get_list_display(request)
        custom_fields = (
            (
                "created",
                "modified",
                "user_created",
                "user_modified",
                "locale_created",
            )
            if self.include_audit_fields_in_list_display
            else ()
        )
        return tuple(f for f in list_display if f not in custom_fields) + custom_fields

    def get_list_filter(self, request) -> tuple[str, ...]:
        """Add audit fields to list display."""
        list_filter = super().get_list_filter(request)
        return tuple(f for f in list_filter if f not in audit_fields) + audit_fields

    def get_readonly_fields(self, request, obj=None) -> tuple[str, ...]:
        """Add audit fields to readonly_fields."""
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        return tuple(f for f in readonly_fields if f not in audit_fields) + audit_fields
