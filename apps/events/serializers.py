from rest_framework import serializers

from apps.events.models import Event
from apps.events.services import event_create


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.EmailField(source="organizer.email", read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "created_at",
            "capacity",
        )
        read_only_fields = ("id", "organizer")


    def create(self, validated_data):
        user = self.context["request"].user
        return event_create(user=user, **validated_data)
