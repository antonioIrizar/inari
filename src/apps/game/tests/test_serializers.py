from django.test import TestCase

from .. import factories, utils
from .. import models
from .. import serializers


class GameSerializerTest(TestCase):
    def test_create(self):
        serializer = serializers.GameSerializer()
        game = serializer.create({})

        self.assertEqual(models.Game.objects.count(), 1)
        self.assertEqual(models.Game.objects.get(uuid=game.uuid), game)

    def test_serializer_data(self):
        game = factories.GameFactory()
        expected = {"uuid": str(game.uuid), "status": game.status}
        serializer = serializers.GameSerializer(instance=game)

        self.assertDictEqual(serializer.data, expected)


class GuessSerializerTest(TestCase):
    def test_create(self):
        game = factories.GameFactory()
        serializer = serializers.GuessSerializer(context={"game": game})
        guess = serializer.create({"guess_code": utils.generate_code()})

        self.assertEqual(models.Guess.objects.count(), 1)
        self.assertEqual(models.Guess.objects.get(guess_code=guess.guess_code), guess)

    def test_serializer_data(self):
        guess = factories.GuessFactory()
        expected = {
            "guess_code": guess.guess_code,
            "correct_color_and_position": guess.correct_color_and_position,
            "correct_color_only": guess.correct_color_only,
            "position": guess.position,
        }
        serializer = serializers.GuessSerializer(instance=guess)

        self.assertDictEqual(serializer.data, expected)


class GameDetailSerializerTest(TestCase):
    def test_serializer_data(self):
        guess = factories.GuessFactory()
        expected = {
            "uuid": str(guess.game.uuid),
            "status": guess.game.status,
            "max_guesses": guess.game.max_guesses,
            "guesses_left": guess.game.guesses_left,
            "guesses": [
                {
                    "guess_code": guess.guess_code,
                    "correct_color_and_position": guess.correct_color_and_position,
                    "correct_color_only": guess.correct_color_only,
                    "position": guess.position,
                }
            ],
        }
        serializer = serializers.GameDetailSerializer(instance=guess.game)
        self.assertDictEqual(serializer.data, expected)

    def test_serializer_data_multiple_guess(self):
        guess_1 = factories.GuessFactory()
        game = guess_1.game
        guess_2 = factories.GuessFactory(game=game)
        expected = {
            "uuid": str(game.uuid),
            "status": game.status,
            "max_guesses": game.max_guesses,
            "guesses_left": game.guesses_left,
            "guesses": [
                {
                    "guess_code": guess_1.guess_code,
                    "correct_color_and_position": guess_1.correct_color_and_position,
                    "correct_color_only": guess_1.correct_color_only,
                    "position": guess_1.position,
                },
                {
                    "guess_code": guess_2.guess_code,
                    "correct_color_and_position": guess_2.correct_color_and_position,
                    "correct_color_only": guess_2.correct_color_only,
                    "position": guess_2.position,
                },
            ],
        }
        serializer = serializers.GameDetailSerializer(instance=game)

        self.assertDictEqual(serializer.data, expected)
