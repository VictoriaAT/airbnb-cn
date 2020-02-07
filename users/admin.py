from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    search_fields = ("username",)

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
