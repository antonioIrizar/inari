from django.test import TestCase

from .. import factories


class GameTestCase(TestCase):
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
