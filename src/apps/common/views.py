from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response


class PingView(generics.GenericAPIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        return Response("pong")
