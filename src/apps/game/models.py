import uuid

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel

from . import managers
from . import settings as game_settings


class AbstractTimeStampedUUID(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Game(AbstractTimeStampedUUID):
    IN_PROGRESS, WON, LOST = "in_progress", "won", "lost"
    STATUS_CHOICES = Choices(
        (IN_PROGRESS, IN_PROGRESS),
        (WON, WON),
        (LOST, LOST),
    )

    secret_code = models.CharField(max_length=game_settings.SECRET_CODE_SIZE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=IN_PROGRESS)
    max_guesses = models.PositiveSmallIntegerField(default=game_settings.MAX_NUMBER_OF_GUESSES)
    guesses_left = models.PositiveSmallIntegerField(default=game_settings.MAX_NUMBER_OF_GUESSES)

    objects = managers.GameManager()

    @property
    def next_position(self) -> int:
        return self.max_guesses - self.guesses_left

    @property
    def is_in_progress(self) -> bool:
        return self.status == self.IN_PROGRESS


class Guess(TimeStampedModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="guesses")
    guess_code = models.CharField(max_length=game_settings.SECRET_CODE_SIZE)
    correct_color_and_position = models.PositiveSmallIntegerField()
    correct_color_only = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()

    objects = managers.GuessManager()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["game", "position"], name="unique_guess_position")]
