from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Відображаємо email замість username у списку
    list_display = ("email", "first_name", "last_name", "is_staff")

    # Додаємо пошук та фільтрацію
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    # Оскільки ми видалили username, нам треба переписати fieldsets,
    # щоб Django не намагався вивести його у формі редагування
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Аналогічно для форми створення користувача
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password"),
            },
        ),
    )
