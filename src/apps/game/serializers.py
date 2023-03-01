from rest_framework import serializers

from . import models
from . import utils


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


class GuessSerializer(serializers.ModelSerializer):
    guess_code = serializers.CharField()

    def validate_guess_code(self, value: str) -> str:
        if not utils.is_valid_secret_code_valid(value):
            raise serializers.ValidationError("guess_code is invalid")
        return value

    def create(self, validated_data: dict) -> models.Guess:
        return models.Guess.objects.create_guess(game=self.context["game"], **validated_data)

    class Meta:
        fields = (
            "guess_code",
            "correct_color_and_position",
            "correct_color_only",
            "position",
        )
        read_only_fields = (
            "correct_color_and_position",
            "correct_color_only",
            "position",
        )
        model = models.Guess


class GameDetailSerializer(serializers.ModelSerializer):
    guesses = GuessSerializer(many=True, read_only=True, source="guesses_ordered_by_position")

    class Meta:
        fields = ("uuid", "status", "max_guesses", "guesses_left", "guesses")
        read_only_fields = fields
        model = models.Game
