from unittest import mock

from django.test import TestCase

from .. import factories
from .. import models
from .. import settings as game_settings
from .. import utils


class GameManagerTest(TestCase):
    def test_create_game(self):
        game = models.Game.objects.create_game()
        self.assertEqual(len(game.secret_code), 4)
        self.assertTrue(all(c in game_settings.SECRET_CODE_CHARACTERS for c in game.secret_code))

    def test_create_game_custom_secret_code(self):
        secret_code = "RBWO"
        game = models.Game.objects.create_game(secret_code)
        self.assertEqual(game.secret_code, secret_code)

    def test_create_game_add_other_model_values(self):
        game = models.Game.objects.create_game(status=models.Game.LOST)
        self.assertEqual(game.status, models.Game.LOST)


class GuessManagerTest(TestCase):
    def test_create_guess(self):
        game = factories.GameFactory()
        with mock.patch("game.utils.check_guess", return_value=(1, 2)) as mock_check_guess:
            guess = models.Guess.objects.create_guess(utils.generate_code(), game)

        mock_check_guess.assert_called_once()
        self.assertEqual(guess.position, 0)
        self.assertEqual(guess.correct_color_and_position, 1)
        self.assertEqual(guess.correct_color_only, 2)

        game.refresh_from_db()
        self.assertTrue(game.is_in_progress)
        self.assertEqual(game.guesses_left, game_settings.MAX_NUMBER_OF_GUESSES - 1)

    def test_create_guess_game_won(self):
        game = factories.GameFactory()
        with mock.patch("game.utils.check_guess", return_value=(4, 0)):
            models.Guess.objects.create_guess(utils.generate_code(), game)

        game.refresh_from_db()
        self.assertFalse(game.is_in_progress)
        self.assertEqual(game.status, models.Game.WON)

    def test_create_guess_game_lost(self):
        game = factories.GameFactory(guesses_left=1)
        with mock.patch("game.utils.check_guess", return_value=(3, 0)):
            models.Guess.objects.create_guess(utils.generate_code(), game)

        game.refresh_from_db()
        self.assertFalse(game.is_in_progress)
        self.assertEqual(game.status, models.Game.LOST)

    def test_create_guess_with_multiple_guess(self):
        game = factories.GameFactory()
        with mock.patch("game.utils.check_guess", return_value=(3, 0)):
            guess_1 = models.Guess.objects.create_guess(utils.generate_code(), game)
            game.refresh_from_db()
            guess_2 = models.Guess.objects.create_guess(utils.generate_code(), game)

        self.assertEqual(guess_1.position, 0)
        self.assertEqual(guess_2.position, 1)
        game.refresh_from_db()
        self.assertEqual(game.guesses_left, game_settings.MAX_NUMBER_OF_GUESSES - 2)
