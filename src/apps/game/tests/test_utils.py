import random

from django.test import TestCase

from .. import settings as game_settings
from .. import utils


class TestIsValidSecretCodeValid(TestCase):
    def test_valid_secret_code(self):
        valid_secret_code = "".join(
            random.choices(game_settings.SECRET_CODE_CHARACTERS, k=game_settings.SECRET_CODE_SIZE)
        )
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
