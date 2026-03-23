import pytest
from django.urls import reverse

from apps.events.models import Event


@pytest.mark.django_db
def test_get_events_list(api_client, user):
    Event.objects.create(
        title="API Test Event",
        capacity=50,
        date="2026-10-01",
        organizer=user
    )

    url = reverse("event-list")
    response = api_client.get(url)

    assert response.status_code == 200

    if isinstance(response.data, dict) and "results" in response.data:
        events = response.data["results"]
    else:
        events = response.data

    assert len(events) >= 1
    assert events[0]["title"] == "API Test Event"


@pytest.mark.django_db
def test_create_event_authenticated(authenticated_client):
    url = reverse('event-list')
    payload = {
        "title": "New Workshop",
        "capacity": 20,
        "date": "2026-11-20",
        "description": "Learn Django",
        "location": "Kyiv Office"
    }

    response = authenticated_client.post(url, data=payload, format='json')

    assert response.status_code == 201
    assert Event.objects.filter(title="New Workshop").exists()
