from django.db import IntegrityError, DatabaseError
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.events.models import Event
from apps.common.utils import database_errors_boundary


def event_create(user, **data) -> Event:
    if data.get("date") and data["date"] < timezone.now():
        raise ValidationError({"date": "Event date cannot be in the past."})

    with database_errors_boundary():
        return Event.objects.create(organizer=user, **data)
