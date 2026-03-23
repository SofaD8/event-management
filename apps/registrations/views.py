from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.events.models import Event
from apps.registrations.serializers import RegistrationSerializer
from apps.registrations.services import register_for_event


class EventRegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        registration = register_for_event(user=request.user, event_id=event.id)
        serializer = self.get_serializer(registration)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
