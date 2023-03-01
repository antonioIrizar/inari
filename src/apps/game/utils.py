import random
import re

from . import settings as game_settings


def is_valid_secret_code_valid(secret_code: str) -> bool:
    return (
        re.fullmatch(
            f"^[{game_settings.SECRET_CODE_CHARACTERS}]{{{game_settings.SECRET_CODE_SIZE}}}$",
            secret_code,
        )
        is not None
    )


def generate_code() -> str:
    return "".join(random.choices(game_settings.SECRET_CODE_CHARACTERS, k=game_settings.SECRET_CODE_SIZE))


def check_guess(secret_code: str, guess_code: str) -> (int, int):
    correct_color_and_position = 0
    correct_color_only = 0
    secret_colors_count = {}
    guess_colors_count = {}

    for i, color in enumerate(secret_code):
        guess_color = guess_code[i]
        if color == guess_color:
            correct_color_and_position += 1
        else:
            secret_colors_count[color] = secret_colors_count.get(color, 0) + 1
            guess_colors_count[guess_color] = guess_colors_count.get(guess_color, 0) + 1

    for color in secret_colors_count.keys():
        correct_color_only += min(secret_colors_count[color], guess_colors_count.get(color, 0))

    return correct_color_and_position, correct_color_only
