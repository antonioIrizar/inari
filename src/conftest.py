import pytest
from django.test import Client


@pytest.fixture(scope="function")
def client() -> Client:
    return Client()
