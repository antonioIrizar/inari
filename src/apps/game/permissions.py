from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsGameInProgress(BasePermission):
    message = "Game is finish"

    def has_permission(self, request: Request, view: APIView) -> bool:
        return view.game.is_in_progress
