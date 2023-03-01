import uuid

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .. import models
from .. import utils
from .. import factories


@pytest.mark.usefixtures("client")
class GameViewTest(TestCase):
    def test_create_game(self):
        response = self.client.post(reverse("game:new-game"), {})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(models.Game.objects.filter(uuid=response.data["uuid"]).exists())


@pytest.mark.usefixtures("client")
class GuessViewTest(TestCase):
    def test_create_guess(self):
        game = factories.GameFactory()
        response = self.client.post(
            reverse("game:new-guess", kwargs={"uuid": game.uuid.hex}), {"guess_code": utils.generate_code()}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(models.Guess.objects.filter(game__uuid=game.uuid).exists())

    def test_create_guess_game_not_exists(self):
        response = self.client.post(
            reverse("game:new-guess", kwargs={"uuid": uuid.uuid4().hex}), {"guess_code": utils.generate_code()}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_guess_game_finish(self):
        game = factories.GameFactory(not_in_progress=True)

        response = self.client.post(
            reverse("game:new-guess", kwargs={"uuid": game.uuid.hex}), {"guess_code": utils.generate_code()}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
