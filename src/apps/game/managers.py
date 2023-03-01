from __future__ import annotations

import random
from typing import TYPE_CHECKING

from django.db import models, transaction

from . import settings as game_settings
from . import utils

if TYPE_CHECKING:
    from .models import Game, Guess


class GameManager(models.Manager):
    def create_game(self, secret_code: str = None, **kwargs) -> Game:
        if secret_code is not None and not utils.is_valid_secret_code_valid(secret_code):
            raise ValueError(f"{secret_code} is not valid")

        secret_code = secret_code or utils.generate_code()

        return self.create(secret_code=secret_code, **kwargs)


class GuessManager(models.Manager):
    @transaction.atomic
    def create_guess(self, guess_code: str, game: Game, **kwargs) -> Guess:
        if not utils.is_valid_secret_code_valid(guess_code):
            raise ValueError(f"{guess_code} is not valid")

        correct_color_and_position, correct_color_only = utils.check_guess(game.secret_code, guess_code)
        position = game.next_position

        game.guesses_left -= 1
        if correct_color_and_position == len(game.secret_code):
            game.status = game.WON
        elif not game.guesses_left:
            game.status = game.LOST

        game.save(
            update_fields=(
                "guesses_left",
                "status",
            )
        )

        return self.create(
            guess_code=guess_code,
            game=game,
            position=position,
            correct_color_and_position=correct_color_and_position,
            correct_color_only=correct_color_only,
            **kwargs,
        )
