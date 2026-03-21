from rest_framework import (
    generics,
    filters,
    permissions
)
from django_filters.rest_framework import DjangoFilterBackend

from apps.events.models import Event
from apps.events.serializers import EventSerializer
from apps.events.services import event_create
from apps.common.permissions import IsOrganizerOrReadOnly


class EventListAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ["location", "organizer"]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["date", "created_at"]

    def perform_create(self, serializer):
        serializer.instance = event_create(
            user=self.request.user,
            **serializer.validated_data
        )


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]
