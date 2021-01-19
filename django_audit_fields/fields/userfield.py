import os
import pwd

from django.db.models import CharField
from django.utils.translation import gettext as _


class UserField(CharField):

    description = _("Custom field for user created")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("blank", True)
        CharField.__init__(self, *args, **kwargs)

    def get_os_username(self):
        return pwd.getpwuid(os.getuid()).pw_name

    def pre_save(self, model_instance, add):
        """Updates username created on ADD only."""
        value = super(UserField, self).pre_save(model_instance, add)
        if not value and not add:
            # fall back to OS user if not accessing through browser
            # better than nothing ...
            value = self.get_os_username()
            setattr(model_instance, self.attname, value)
            return value
        return value
