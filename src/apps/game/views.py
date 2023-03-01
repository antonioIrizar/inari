from functools import cached_property

from rest_framework import generics

from . import serializers
from . import models
from . import permissions


class GameView(generics.CreateAPIView):
    serializer_class = serializers.GameSerializer


class GameDetailView(generics.RetrieveAPIView):
    lookup_url_kwarg = "uuid"
    lookup_field = "uuid"
    serializer_class = serializers.GameDetailSerializer
    queryset = models.Game


class GuessView(generics.CreateAPIView):
    permission_classes = [permissions.IsGameInProgress]
    serializer_class = serializers.GuessSerializer
    lookup_url_kwarg = "uuid"

    @cached_property
    def game(self) -> models.Game:
        return generics.get_object_or_404(
            models.Game,
            uuid=self.kwargs[self.lookup_url_kwarg],
        )

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context["game"] = self.game
        return context
