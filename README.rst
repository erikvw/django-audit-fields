|pypi| |actions| |codecov| |downloads| |clinicedc|


django-audit-fields
===================

`django-audit-fields.readthedocs.io <https://django-audit-fields.readthedocs.io/>`_

DJ5.2+, py3.12+

Important:
    * As of version 1.1.0, `edc-utils`_ is no longer a dependency of ``django-audit-fields``.


This module includes `django-revision`_ and is best used together with `django-simple-history`_.

Older versions
--------------
* <=0.3.3 (DJ 3.1, py 3.7, 3.8)
* >=0.3.4 (DJ 3.2+, py 3.9+)
* >=0.3.14 (DJ4.2, py3.11) includes locale


Installation
------------

.. code-block:: bash

    pip install django-audit-fields

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
    from simple_history.models import HistoricalRecords

    class MyModel(AuditModelMixin,  models.Model):

        history = HistoricalRecord()

        class Meta(AuditModelMixin.Meta):
            pass

Preferably, use a UUID as primary key by declaring your model using ``AuditUuidModelMixin``

.. code-block:: python

    from django_audit_fields.model_mixins import AuditUuidModelMixin
    from simple_history.models import HistoricalRecords

    class MyModel(AuditUuidModelMixin, models.Model):

        history = HistoricalRecord()

        class Meta(AuditUuidModelMixin.Meta):
            pass


Model mixins ``AuditModelMixin`` and ``AuditUuidModelMixin``
------------------------------------------------------------

The model mixin ``AuditUuidModelMixin`` sets the ``id`` fields to a ``UUIDField`` instead of an integer field.

Model mixins ``AuditModelMixin`` and ``AuditUuidModelMixin`` add audit fields:

+-------------------+-----------------+----------------------------+
| Field             | Field class     | Update event               |
+===================+=================+============================+
| created           | DateTimeField   | only set on pre-save add   |
+-------------------+-----------------+----------------------------+
| modified          | DateTimeField   | updates on every save      |
+-------------------+-----------------+----------------------------+
| user_created      | CharField       | only set on pre-save add   |
+-------------------+-----------------+----------------------------+
| user_modified     | CharField       | updates on every save      |
+-------------------+-----------------+----------------------------+
| hostname_created  | CharField       | only set on pre-save add   |
+-------------------+-----------------+----------------------------+
| hostname_modified | CharField       | updates on every save      |
+-------------------+-----------------+----------------------------+
| locale_created    | CharField       | only set on pre-save add   |
+-------------------+-----------------+----------------------------+
| locale_modified   | CharField       | updates on every save      |
+-------------------+-----------------+----------------------------+
| revision          | RevisionField*  | updates on every save      |
+-------------------+-----------------+----------------------------+


* RevisionField is from django-revision. See `django-revision.readthedocs.io <https://django-revision.readthedocs.io/>`_.


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
.. _edc-utils: https://github.com/clinicedc/edc-utils
.. _django-simple-history: https://github.com/django-commons/django-simple-history
