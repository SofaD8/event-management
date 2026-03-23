from django.conf import settings
from django.db import models

from apps.common.models import BaseModel


class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_events",
    )
    capacity = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
