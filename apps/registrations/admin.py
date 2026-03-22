from django.contrib import admin

from apps.registrations.models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event", "created_at")
    list_filter = ("event", "created_at")
    search_fields = ("user__email", "event__title")
    readonly_fields = ("created_at", "updated_at")
