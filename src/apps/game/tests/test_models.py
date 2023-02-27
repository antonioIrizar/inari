import random

from django.db import IntegrityError, DataError
from django.test import TransactionTestCase

from .. import factories
from ..settings import SECRET_CODE_CHARACTERS, SECRET_CODE_SIZE


class GameTestCase(TransactionTestCase):
    def test_create_game(self):
        game = factories.GameFactory()
        self.assertEqual(game.status, game.IN_PROGRESS)
        self.assertEqual(len(game.secret_code), 4)

    def test_game_violates_constraint(self):
        test_cases = ["1234", "".join(random.choices(SECRET_CODE_CHARACTERS, k=2))]

        for secret_code in test_cases:
            with self.subTest(), self.assertRaisesMessage(
                IntegrityError, 'violates check constraint "secret_code_regex"'
            ):
                factories.GameFactory(secret_code=secret_code)

    def test_game_secret_code_not_have_more_size(self):
        with self.assertRaisesMessage(DataError, "value too long for type character"):
            factories.GameFactory(secret_code="".join(random.choices(SECRET_CODE_CHARACTERS, k=SECRET_CODE_SIZE + 1)))
