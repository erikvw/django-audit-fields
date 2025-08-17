|pypi| |actions| |codecov| |downloads| |clinicedc|


django-audit-fields
===================

DJ5.2+, py3.12+

Important:
    As of version 1.1.0, `edc-utils`_ is no longer a dependency of ``django-audit-fields``. You may also exclude the model mixin from `django-revision`_ in ``settings``. See `the example below`_.

Older VERSIONS
--------------
* <=0.3.3 (DJ 3.1, py 3.7, 3.8)
* >=0.3.4 (DJ 3.2+, py 3.9+)
* >=0.3.14 (DJ4.2, py3.11) includes locale


Installation
------------

.. code-block:: bash

    pip install django-audit-fields

If you wish to keep the old behaviour where ``AuditModelMixin`` and ``AuditUuidModelMixin`` are declared with the ``RevisionModelMixin`` from django_revision:

.. code-block:: bash

    pip install django-audit-fields[django-revision]

or just install separately

.. code-block:: bash

    pip install django-audit-fields
    pip install django-revision

Add ``django-audit-fields`` to INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = [
        "...",
        "django_audit_fields.apps.AppConfig",
        "..."]

Usage
-----

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
        # ...
        class Meta(AuditUuidModelMixin.Meta):
            pass

The model mixins ``AuditModelMixin`` and ``AuditUuidModelMixin``:

* add audit fields (created, modified, user_created, user_modified, hostname_created, hostname_modified);

The model mixin ``AuditUuidModelMixin`` also

* sets the id fields to a ``UUIDField`` instead of an integer;

.. _the example below:

RevisionModelMixin from django-revision is included by default
..............................................................

By default ``AuditModelMixin`` and ``AuditUuidModelMixin`` are declared with the modelmixin ``RevisionModelMixin`` from `django-revision`_. If you do not want this behaviour, use the settings attribute in the example below to exclude the mixin. By default ``DJANGO_AUDIT_FIELDS_INCLUDE_REVISION`` is set to ``True``.

To not use ``RevisionModelMixin``

.. code-block:: python

    DJANGO_AUDIT_FIELDS_INCLUDE_REVISION = False


Warning:
    setting DJANGO_AUDIT_FIELDS_INCLUDE_REVISION to ``False`` will trigger a migration to remove model field ``revision`` for existing models.

Adding ``RevisionModelMixin`` back when ``DJANGO_AUDIT_FIELDS_INCLUDE_REVISION = False``

.. code-block:: python

    from simple_history.models import HistoricalRecords
    from django_revision.modelmixins import RevisionModelMixin

    class MyModel(AuditUuidModelMixin, RevisionModelMixin, models.Model):
        # ...
        history = HistoricalRecords()



Adding the HistoricalRecords manager from django-simple-history
...............................................................

Consider configuring your models with the ``HistoricalRecord`` model manager from `django-simple-history`_

.. code-block:: python

    from simple_history.models import HistoricalRecords

    class MyModel(AuditUuidModelMixin, models.Model):
        # ...
        history = HistoricalRecords()




Notes
-----

User created and modified fields behave as follows:

* created is only set on pre-save add
* modified is always updated


.. |pypi| image:: https://img.shields.io/pypi/v/django-audit-fields.svg
   :target: https://pypi.python.org/pypi/django-audit-fields

.. |codecov| image:: https://codecov.io/gh/erikvw/django-audit-fields/branch/develop/graph/badge.svg
   :target: https://codecov.io/gh/erikvw/django-audit-fields

.. |downloads| image:: https://pepy.tech/badge/django-audit-fields
   :target: https://pepy.tech/project/django-audit-fields

.. |actions| image:: https://github.com/erikvw/django-audit-fields/actions/workflows/build.yml/badge.svg
   :target: https://github.com/erikvw/django-audit-fields/actions/workflows/build.yml

.. |clinicedc| image:: https://img.shields.io/badge/framework-Clinic_EDC-green
   :alt:Made with clinicedc
   :target: https://github.com/clinicedc

.. _django-revision: https://github.com/erikvw/django-revision
.. _edc-utils: https://github.com/erikvw/edc-utils
.. _django-simple-history: https://github.com/django-commons/django-simple-history
