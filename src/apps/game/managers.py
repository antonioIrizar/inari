from __future__ import annotations

import random
from typing import TYPE_CHECKING

from django.db import models

from . import settings as game_settings

if TYPE_CHECKING:
    from .models import Game


class GameManager(models.Manager):
    def create_game(self, secret_code: str = None, **kwargs) -> Game:
        secret_code = secret_code or "".join(
            random.choices(
                game_settings.SECRET_CODE_CHARACTERS, k=game_settings.SECRET_CODE_SIZE
            )
        )

        return self.create(secret_code=secret_code, **kwargs)
