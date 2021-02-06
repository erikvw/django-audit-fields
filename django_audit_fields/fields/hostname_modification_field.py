import socket

from django.db.models import CharField
from django.utils.translation import gettext as _


class HostnameModificationField(CharField):

    description = _("Custom field for hostname modified")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("blank", True)
        CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        """Updates socket.gethostname() on each save."""
        value = socket.gethostname()
        setattr(model_instance, self.attname, value)
        return value
