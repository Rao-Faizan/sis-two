# admin.py
from django.contrib import admin
from .models import Grade, Section, ClassRoom


# --- Inline for ClassRoom ---
class ClassRoomInline(admin.TabularInline):
    model = ClassRoom
    extra = 1


# --- Section Admin ---
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "grade", "class_teacher", "campus", "capacity")
    list_filter = ("grade", "campus")
    search_fields = ("name", "grade__name", "class_teacher__name", "campus__campus_name")
    filter_horizontal = ("students",)  # ManyToMany ko better banata hai
    inlines = [ClassRoomInline]


# --- Grade Admin ---
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "campus")
    list_filter = ("campus",)
    search_fields = ("name", "campus__campus_name")


# --- ClassRoom Admin ---from django.contrib import admin
from .models import Grade, Section, ClassRoom


# --- Inline for ClassRoom ---
class ClassRoomInline(admin.TabularInline):
    model = ClassRoom
    extra = 1


# --- Section Admin ---
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "grade", "class_teacher", "capacity")
    list_filter = ("grade__campus", "grade")  # Fixed line
    search_fields = ("name", "grade__name", "class_teacher__name")
    filter_horizontal = ("students",)


    # helper method to show campus in list_display
    def get_campus(self, obj):
        return obj.campus.campus_name
    get_campus.short_description = "Campus"   # column heading


# --- Grade Admin ---
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "campus")
    list_filter = ("campus",)
    search_fields = ("name", "campus__campus_name")


# --- ClassRoom Admin ---
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "capacity")
    list_filter = ("section",)   # ✅ section__campus hata diya
    search_fields = ("name", "section__name", "section__grade__name")


# Register Models
admin.site.register(Grade, GradeAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "capacity")
    list_filter = ("section__grade", "section__campus")
    search_fields = ("name", "section__name", "section__grade__name")


# # Register Models
# admin.site.register(Grade, GradeAdmin)
# admin.site.register(Section, SectionAdmin)
# admin.site.register(ClassRoom, ClassRoomAdmin)
