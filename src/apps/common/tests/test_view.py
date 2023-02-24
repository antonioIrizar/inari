from django.test import Client
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class PingViewTest(TestCase):
    def test_ping(self):
        client = Client()
        response = client.get(reverse("common:ping"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
