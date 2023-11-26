"""
Views for the user and API.
"""

from rest_framework import generics
from user.serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        response_data = {
            "status": 'Created Successfully'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
