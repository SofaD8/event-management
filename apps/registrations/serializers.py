from rest_framework import serializers

from apps.registrations.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)
    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Registration
        fields = ("id", "user_email", "event_title", "created_at")
