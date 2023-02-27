from .base import *  # noqa: F401, F403
import os

ENVIRONMENT_NAME = "test"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres_test",
        "USER": os.getenv("DB_USER", os.getenv("DB_USER", "inari")),
        "PASSWORD": os.getenv("DB_PASSWORD", os.getenv("DB_PASSWORD", "root")),
        "HOST": os.getenv("DB_HOST", os.getenv("DB_HOST", "postgres14")),
        "PORT": os.getenv("DB_PORT", os.getenv("DB_PORT", "5432")),
    }
}
