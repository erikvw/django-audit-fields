#!/usr/bin/env python
import sys
from pathlib import Path

from edc_test_settings.default_test_settings import DefaultTestSettings

app_name = "django_audit_fields"
base_dir = Path(__file__).absolute().parent.parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=base_dir / "tests" / "etc",
    DJANGO_AUDIT_FIELDS_INCLUDE_REVISION=False,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        f"{app_name}.apps.AppConfig",
    ],
    use_test_urls=True,
).settings


for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
