from django.urls import path
from apps.registrations.views import EventRegistrationView


urlpatterns = [
    path("<int:event_id>/register/", EventRegistrationView.as_view(), name="event-register"),
]
