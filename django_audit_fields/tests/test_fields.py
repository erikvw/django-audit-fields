import os
import pwd
import re
import socket

from django.test import TestCase

from .models import TestModel


class TestFields(TestCase):
    def setUp(self):
        self.uuid_regex = re.compile(
            "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"
        )

    def test_uuid_none_on_instance(self):
        test_model = TestModel()
        self.assertIsNone(test_model.id)

    def test_uuid_set_on_create(self):
        test_model = TestModel.objects.create()
        self.assertIsNotNone(test_model.pk)
        self.assertTrue(re.match(self.uuid_regex, str(test_model.pk)))

    def test_uuid_set_on_save(self):
        test_model = TestModel()
        self.assertIsNone(test_model.id)
        test_model.save()
        self.assertTrue(re.match(self.uuid_regex, str(test_model.pk)))

    def test_uuid_unique(self):
        test_model1 = TestModel.objects.create(f1="monday")
        self.assertIsNotNone(test_model1.id)
        self.assertTrue(re.match(self.uuid_regex, str(test_model1.pk)))
        test_model2 = TestModel.objects.create(f1="tuesday")
        self.assertIsNotNone(test_model2.id)
        self.assertTrue(re.match(self.uuid_regex, str(test_model2.pk)))
        test_model3 = TestModel(f1="wednesday")
        self.assertIsNone(test_model3.id)
        test_model3.save()
        self.assertTrue(re.match(self.uuid_regex, str(test_model3.pk)))
        self.assertFalse(test_model1.pk == test_model2.pk)
        self.assertFalse(test_model2.pk == test_model3.pk)

    def test_hostname_modification(self):
        hostname = socket.gethostname()
        test_model = TestModel()
        self.assertFalse(test_model.hostname_modified)
        test_model = TestModel.objects.create()
        self.assertIsInstance(test_model.hostname_modified, str)
        self.assertEqual(hostname, test_model.hostname_modified)
        test_model.save()
        self.assertEqual(hostname, test_model.hostname_modified)

    def test_hostname_created(self):
        hostname = socket.gethostname()
        test_model = TestModel(f1="monday")
        self.assertIsNotNone(test_model.hostname_created)
        self.assertEqual(hostname, test_model.hostname_created)
        test_model = TestModel.objects.create(f1="tuesday")
        self.assertEqual(hostname, test_model.hostname_created)
        test_model.save()
        self.assertEqual(hostname, test_model.hostname_created)

    def test_user_created(self):
        """Assert user is set on created ONLY unless explicitly set.
        """
        pwd.getpwuid(os.getuid()).pw_name
        test_model = TestModel.objects.create(f1="monday")
        self.assertEqual("", test_model.user_created)
        test_model.user_created = ""
        test_model.save()
        test_model = TestModel(f1="tuesday", user_created="jason")
        test_model.save()
        self.assertEqual("jason", test_model.user_created)
        test_model.save()
        self.assertEqual("jason", test_model.user_created)

    def test_user_modified(self):
        """Assert user is always updated.
        """
        user = pwd.getpwuid(os.getuid()).pw_name
        test_model = TestModel(f1="monday")
        test_model.save()
        self.assertEqual("", test_model.user_modified)
        test_model = TestModel.objects.create(f1="tuesday")
        self.assertEqual("", test_model.user_modified)
        test_model.user_modified = ""
        test_model.save()
        self.assertEqual(user, test_model.user_modified)
