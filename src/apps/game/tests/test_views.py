import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .. import models


@pytest.mark.usefixtures("client")
class GameViewTest(TestCase):
    def test_create_Game(self):
        response = self.client.post(reverse("game:new-game"), {})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(models.Game.objects.filter(uuid=response.data["uuid"]).exists())
