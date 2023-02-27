from rest_framework import generics

from . import serializers


class GameView(generics.CreateAPIView):
    serializer_class = serializers.GameSerializer
