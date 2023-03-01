import factory
from factory.fuzzy import FuzzyChoice
from . import models
from . import utils


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Game

    @classmethod
    def _create(cls, model_class: models.Game, *args, **kwargs) -> models.Game:
        manager = cls._get_manager(model_class)
        return manager.create_game(*args, **kwargs)

    class Params:
        not_in_progress = factory.Trait(status=FuzzyChoice((models.Game.LOST, models.Game.WON)))


class GuessFactory(factory.django.DjangoModelFactory):
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Guess

    @classmethod
    def _create(cls, model_class: models.Guess, *args, **kwargs) -> models.Game:
        manager = cls._get_manager(model_class)
        guess_code = kwargs.pop("guess_code", utils.generate_code())
        return manager.create_guess(guess_code, *args, **kwargs)
