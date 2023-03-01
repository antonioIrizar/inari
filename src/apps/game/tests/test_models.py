from django.db import IntegrityError
from django.test import TestCase

from .. import factories
from .. import models
from .. import settings as game_settings
from .. import utils


class GameTest(TestCase):
    def test_create_game(self):
        game = factories.GameFactory()
        self.assertEqual(game.status, game.IN_PROGRESS)
        self.assertEqual(len(game.secret_code), 4)

    def test_game_secret_code_invalid(self):
        test_cases = [
            "",
            "1234",
        ]

        for secret_code in test_cases:
            with self.subTest(), self.assertRaisesMessage(ValueError, f"{secret_code} is not valid"):
                factories.GameFactory(secret_code=secret_code)


class GuessTest(TestCase):
    def test_guess(self):
        guess = factories.GuessFactory()
        self.assertEqual(len(guess.guess_code), game_settings.SECRET_CODE_SIZE)

    def test_guess_with_custom_code(self):
        guess_code = utils.generate_code()
        guess = factories.GuessFactory(guess_code=guess_code)
        self.assertEqual(guess.guess_code, guess_code)

    def test_guess_invalid_constraint(self):
        guess = factories.GuessFactory()
        with self.assertRaisesMessage(
            IntegrityError, 'duplicate key value violates unique constraint "unique_guess_position"'
        ):
            models.Guess.objects.create(
                game=guess.game,
                position=guess.position,
                guess_code=utils.generate_code(),
                correct_color_and_position=0,
                correct_color_only=0,
            )
