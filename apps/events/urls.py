from django.urls import path

from apps.events.views import EventListAPIView, EventDetailAPIView


urlpatterns = [
    path(
        "",
        EventListAPIView.as_view(),
        name="event-list"
    ),
    path(
        "<int:pk>/",
        EventDetailAPIView.as_view(),
        name="event-detail"
    ),
]
