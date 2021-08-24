from edc_utils import get_utcnow

from .constants import AUDIT_MODEL_FIELDS

audit_fields = AUDIT_MODEL_FIELDS

audit_fieldset_tuple = ("Audit", {"classes": ("collapse",), "fields": AUDIT_MODEL_FIELDS})


class ModelAdminAuditFieldsMixin:
    def save_model(self, request, obj, form, change) -> None:
        """Update audit fields from request object before save."""
        if not change:
            obj.user_created = request.user.username
            obj.created = get_utcnow()
        else:
            obj.user_modified = request.user.username
            obj.modified = get_utcnow()
        super().save_model(request, obj, form, change)

    def get_list_filter(self, request) -> tuple:
        """Add audit fields to end of list display."""
        list_filter = super().get_list_filter(request)
        list_filter = [
            f for f in list_filter if f not in AUDIT_MODEL_FIELDS
        ] + AUDIT_MODEL_FIELDS
        if list_filter:
            return tuple(list_filter)
        return tuple()

    def get_readonly_fields(self, request, obj=None) -> tuple:
        """Add audit fields to readonly_fields."""
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        readonly_fields = list(readonly_fields) + [
            f for f in AUDIT_MODEL_FIELDS if f not in readonly_fields
        ]
        return tuple(readonly_fields)
