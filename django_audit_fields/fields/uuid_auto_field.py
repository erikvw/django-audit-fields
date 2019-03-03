import uuid

from django.db.models.fields import UUIDField


class UUIDAutoField(UUIDField):
    """ AutoField for Universally unique identifier.
    """

    def pre_save(self, model_instance, add):
        value = super(UUIDAutoField, self).pre_save(model_instance, add)
        if add and value is None:
            value = uuid.uuid4()
            setattr(model_instance, self.attname, value)
        else:
            if not value:
                value = uuid.uuid4()
                setattr(model_instance, self.attname, value)
        return value
