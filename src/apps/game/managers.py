from __future__ import annotations

import random
from typing import TYPE_CHECKING

from django.db import models

from . import settings as game_settings
from .utils import is_valid_secret_code_valid

if TYPE_CHECKING:
    from .models import Game


class GameManager(models.Manager):
    def create_game(self, secret_code: str = None, **kwargs) -> Game:
        if secret_code is not None and not is_valid_secret_code_valid(secret_code):
            raise ValueError(f"{secret_code} is not valid")

        secret_code = secret_code or "".join(
            random.choices(game_settings.SECRET_CODE_CHARACTERS, k=game_settings.SECRET_CODE_SIZE)
        )

        return self.create(secret_code=secret_code, **kwargs)
