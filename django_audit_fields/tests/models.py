from django.db import models

from ..models import AuditUuidModelMixin


class TestModel(AuditUuidModelMixin):

    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)
    f3 = models.CharField(max_length=10, null=True, blank=False)
    f4 = models.CharField(max_length=10, null=True, blank=False)
    f5 = models.CharField(max_length=10)
    f5_other = models.CharField(max_length=10, null=True)
