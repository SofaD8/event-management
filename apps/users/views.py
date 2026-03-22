from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import UserSerializer, UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    """Ендпоінт для реєстрації нового користувача."""
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserMeView(generics.RetrieveUpdateAPIView):
    """Ендпоінт для отримання/редагування власного профілю."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Повертаємо поточного залогіненого юзера
        return self.request.user
