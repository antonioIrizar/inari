from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from . import models


class IsGameInProgress(BasePermission):
    message = "Game is finish"

    def has_permission(self, request: Request, view: APIView) -> bool:
        return view.game.is_in_progress


class IsGameObjectInProgress(BasePermission):
    message = "Game is finish"

    def has_object_permission(self, request, view, obj: models.Game) -> bool:
        return obj.is_in_progress
