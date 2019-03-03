|pypi| |travis| |codecov| |downloads|

django-audit-fields
-------------------

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

* add audit fields (user_created, user_modified, date_created, etc);

The model mixin ``AuditUuidModelMixin`` also

* sets the id fields to a ``UUIDField`` instead of an integer;


Most models require an audit trail. If so, add the ``HistoricalRecord`` model manager from ``django-simple-history``:

.. code-block:: python

    from edc_model.model.models import HistoricalRecord
    
    class MyModel(AuditUuidModelMixin, models.Model):
        
        ...
        history = HistoricalRecord()
        

Notes
-----

User created and modified fields behave as follows:

* created is only set on pre-save add
* modified is always updated


.. |pypi| image:: https://img.shields.io/pypi/v/django-audit-fields.svg
    :target: https://pypi.python.org/pypi/django-audit-fields
    
.. |travis| image:: https://travis-ci.org/erikvw/django-audit-fields.svg?branch=develop
    :target: https://travis-ci.org/erikvw/django-audit-fields
    
.. |codecov| image:: https://codecov.io/gh/erikvw/django-audit-fields/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/erikvw/django-audit-fields

.. |downloads| image:: https://pepy.tech/badge/django-audit-fields
   :target: https://pepy.tech/project/django-audit-fields
