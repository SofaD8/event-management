from django.contrib import admin

from apps.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location", "organizer", "created_at")
    list_filter = ("date", "organizer", "location")
    search_fields = ("title", "description", "location")
    sortable_by = ("date")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.organizer = request.user
        super().save_model(request, obj, form, change)
