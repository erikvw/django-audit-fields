|pypi| |actions| |codecov| |downloads|

django-audit-fields
-------------------

VERSION
=======
* <=0.3.3 (DJ 3.1, py 3.7, 3.8)
* >=0.3.4 (DJ 3.2+, py 3.9+)


Installation
============

.. code-block:: bash

    pip install django_audit_fields


Add both ``django_audit_fields`` and ``django_revision`` to INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = [
        "...",
        "django_revision.apps.AppConfig",
        "django_audit_fields.apps.AppConfig",
        "..."]

Usage
=====

Add model fields to track creation and modification dates, users and more on save.


Declare your model using ``AuditModelMixin``

.. code-block:: python

    from django_audit_fields.model_mixins import AuditModelMixin

    class MyModel(AuditModelMixin,  models.Model):
        ...
        class Meta(AuditModelMixin.Meta):
            pass

Preferably, use a UUID as primary key by declaring your model using ``AuditUuidModelMixin``

.. code-block:: python

    from django_audit_fields.model_mixins import AuditUuidModelMixin

    class MyModel(AuditUuidModelMixin, models.Model):
        ...
        class Meta(AuditUuidModelMixin.Meta)
            pass

The model mixins ``AuditModelMixin`` and ``AuditUuidModelMixin``:

* add audit fields (created, modified, user_created, user_modified, hostname_created, hostname_modified);

The model mixin ``AuditUuidModelMixin`` also

* sets the id fields to a ``UUIDField`` instead of an integer;


Most models require an audit trail. If so, add the ``HistoricalRecord`` model manager from ``django-simple-history``:

.. code-block:: python

    from simple_history.models import HistoricalRecords

    class MyModel(AuditUuidModelMixin, models.Model):
        ...
        history = HistoricalRecords()

Notes
=====

User created and modified fields behave as follows:

* created is only set on pre-save add
* modified is always updated


.. |pypi| image:: https://img.shields.io/pypi/v/django-audit-fields.svg
    :target: https://pypi.python.org/pypi/django-audit-fields

.. |codecov| image:: https://codecov.io/gh/erikvw/django-audit-fields/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/erikvw/django-audit-fields

.. |downloads| image:: https://pepy.tech/badge/django-audit-fields
   :target: https://pepy.tech/project/django-audit-fields

.. |actions| image:: https://github.com/erikvw/django-audit-fields/workflows/build/badge.svg?branch=develop
  :target: https://github.com/erikvw/django-audit-fields/actions?query=workflow:build
