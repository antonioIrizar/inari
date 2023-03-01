from django.urls import path

from . import views


urlpatterns = [
    path("game/", views.GameView.as_view(), name="new-game"),
    path("game/<uuid>/guess/", views.GuessView.as_view(), name="new-guess"),
]
