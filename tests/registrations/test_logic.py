import pytest

from apps.common.exceptions import EventFullException, UserAlreadyExistsException
from apps.events.models import Event
from apps.registrations.services import register_for_event


@pytest.mark.django_db
def test_registration_increases_event_occupancy(user):
    event = Event.objects.create(
        title="PyCon",
        capacity=10,
        date="2026-05-01",
        organizer = user
    )
    register_for_event(user=user, event_id=event.id)
    assert event.participants.count() == 1


@pytest.mark.django_db
def test_registration_fails_when_event_is_full(user):
    event = Event.objects.create(
        title="Sold Out Event",
        capacity=0,
        date="2026-06-01",
        organizer=user
    )

    with pytest.raises(EventFullException):
        register_for_event(user=user, event_id=event.id)


@pytest.mark.django_db
def test_cannot_register_for_same_event_twice(user):
    event = Event.objects.create(
        title="Double Reg Test",
        capacity=5,
        date="2026-07-01",
        organizer=user
    )

    register_for_event(user=user, event_id=event.id)

    with pytest.raises(UserAlreadyExistsException):
        register_for_event(user=user, event_id=event.id)
