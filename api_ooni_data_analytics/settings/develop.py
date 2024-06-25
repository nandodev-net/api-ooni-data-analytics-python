"""Development workspace settings."""

import os

from api_ooni_data_analytics.settings.base import *  # pylint: disable=wildcard-import,unused-wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split()
