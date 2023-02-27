import factory
from . import models


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Game

    @classmethod
    def _create(cls, model_class: models.Game, *args, **kwargs) -> models.Game:
        manager = cls._get_manager(model_class)
        return manager.create_game(*args, **kwargs)
