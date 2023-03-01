import random

from django.test import TestCase

from .. import settings as game_settings
from .. import utils


class IsValidSecretCodeValidTest(TestCase):
    def test_valid_secret_code(self):
        valid_secret_code = utils.generate_code()
        self.assertTrue(utils.is_valid_secret_code_valid(valid_secret_code))

    def test_invalid_secret_code(self):
        test_cases = [
            "ABCD",
            game_settings.SECRET_CODE_CHARACTERS * (game_settings.SECRET_CODE_SIZE - 1),
            game_settings.SECRET_CODE_CHARACTERS * (game_settings.SECRET_CODE_SIZE + 1),
            "",
        ]
        for secret_code in test_cases:
            with self.subTest():
                self.assertFalse(utils.is_valid_secret_code_valid(secret_code))


class CheckGuessTest(TestCase):
    def test_check_guess(self):
        test_cases = [
            ("RGGB", "RGGB", 4, 0),
            ("RRRR", "BYOB", 0, 0),
            ("GBBR", "GBRB", 2, 2),
            ("BBBR", "RBGG", 1, 1),
            ("RBGG", "BBBR", 1, 1),
            ("BBBR", "BBBR", 4, 0),
            ("WBWB", "BWBW", 0, 4),
            ("OOOW", "OWWW", 2, 0),
        ]

        for secret_code, guess_code, correct_color_and_position, correct_color_only in test_cases:
            with self.subTest(msg=f"{secret_code} {guess_code}"):
                self.assertEqual(
                    utils.check_guess(secret_code, guess_code),
                    (
                        correct_color_and_position,
                        correct_color_only,
                    ),
                )


class GenerateCodeTest(TestCase):
    def test_generate_code(self):
        code = utils.generate_code()

        self.assertTrue(set(code).issubset(set(game_settings.SECRET_CODE_CHARACTERS)))
        self.assertEqual(len(code), game_settings.SECRET_CODE_SIZE)
