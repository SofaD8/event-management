from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.events.models import Event
from apps.common.exceptions import BaseAPIException


class EventDateInPastException(BaseAPIException):
    default_detail = _("Event date cannot be in the past.")
    default_code = "event_date_invalid"


def event_create(user, **data) -> Event:
    event_date = data.get("date")

    if event_date and event_date < timezone.now():
        raise EventDateInPastException()

    return Event.objects.create(organizer=user, **data)
