from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    # List view me kya columns dikhne chahiye
    list_display = ("name", "section", "campus", "class_teacher", "capacity")

    # Filtering options sidebar me
    list_filter = ("campus", "name", "section", "class_teacher")

    # Search bar ke liye fields
    search_fields = ("name", "section", "campus__name", "class_teacher__teacher__first_name")

    # Related objects ke liye autocomplete
    autocomplete_fields = ("campus", "class_teacher")

    # Ordering (admin panel me by default sort)
    ordering = ("campus", "name", "section")

    # Extra configuration (optional, UX better ke liye)
    list_per_page = 25
    save_as = True
    save_on_top = True
