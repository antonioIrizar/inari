from django.test import TestCase

from .. import factories
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
