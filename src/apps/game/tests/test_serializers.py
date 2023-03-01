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
