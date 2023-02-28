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

    objects = managers.GameManager()
