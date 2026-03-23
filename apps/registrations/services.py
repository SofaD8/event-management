from django.db import transaction

from apps.common.exceptions import EventFullException, UserAlreadyExistsException
from apps.common.utils import send_app_email
from apps.events.models import Event
from apps.registrations.models import Registration


@transaction.atomic
def register_for_event(user, event_id) -> Registration:
    event = Event.objects.select_for_update().get(id=event_id)

    if Registration.objects.filter(user=user, event=event).exists():
        raise UserAlreadyExistsException()

    if event.participants.count() >= event.capacity:
        raise EventFullException()

    registration = Registration.objects.create(user=user, event=event)

    send_app_email(
        subject=f"You are registered: {event.title}",
        message=f"Congratulations! "
                f"You have successfully registered for the event '{event.title}', "
                f"which will take place on {event.date}.",
        recipient_list=[user.email]
    )

    return registration
