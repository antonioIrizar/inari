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
