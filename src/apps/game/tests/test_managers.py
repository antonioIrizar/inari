from django.test import TestCase

from .. import models
from .. import settings


class GameManagerTest(TestCase):
    def test_create_game(self):
        game = models.Game.objects.create_game()
        self.assertEqual(len(game.secret_code), 4)
        self.assertTrue(all(c in settings.SECRET_CODE_CHARACTERS for c in game.secret_code))

    def test_create_game_custom_secret_code(self):
        secret_code = "RBWO"
        game = models.Game.objects.create_game(secret_code)
        self.assertEqual(game.secret_code, secret_code)

    def test_create_game_add_other_model_values(self):
        game = models.Game.objects.create_game(status=models.Game.LOST)
        self.assertEqual(game.status, models.Game.LOST)
