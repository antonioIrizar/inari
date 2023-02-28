from rest_framework import serializers

from . import models


class GameSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> models.Game:
        return models.Game.objects.create_game(**validated_data)

    class Meta:
        fields = (
            "uuid",
            "status",
        )
        read_only_fields = fields
        model = models.Game
