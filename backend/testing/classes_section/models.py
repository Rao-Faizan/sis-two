from django.db import models
from campus.models import Campus
from teachers.models import TeacherRole


# ===================== Grade (Class + Section) =====================
class Grade(models.Model):
    # Basic Information
    name = models.CharField(max_length=50, help_text="Class/Grade name e.g. Grade 3, O-Level")
    section = models.CharField(max_length=20, help_text="Section name e.g. A, B, C")
    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, related_name="grades"
    )

    # Class Type (Regular, Prep, Montessori, etc.)
    category = models.CharField(
        max_length=50,
        choices=[
            ("Regular", "Regular"),
            ("Prep", "Prep"),
            ("Montessori", "Montessori"),
            ("Other", "Other"),
        ],
        default="Regular",
        help_text="Type of class (Regular, Prep, Montessori, etc.)"
    )

    # Combined Classes
    is_combined = models.BooleanField(default=False, help_text="Is this a combined class?")
    combined_with = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="If combined, mention with which grade e.g. Class 5"
    )

    # Class Teacher
    class_teacher = models.ForeignKey(
        TeacherRole,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Assign a class teacher"
    )

    # Capacity / Strength
    capacity = models.PositiveIntegerField(default=30, help_text="Maximum number of students allowed")
    enrolled_students = models.PositiveIntegerField(default=0, help_text="Current enrolled students")
    total_boys = models.PositiveIntegerField(default=0, help_text="Number of boys in this class")
    total_girls = models.PositiveIntegerField(default=0, help_text="Number of girls in this class")
    avg_class_size = models.PositiveIntegerField(default=0, help_text="Average number of students in this section")

    # Academic Details
    subjects = models.TextField(
        blank=True,
        null=True,
        help_text="Comma separated list of subjects offered in this class"
    )
    medium_of_instruction = models.CharField(
        max_length=50,
        choices=[
            ("English", "English"),
            ("Urdu", "Urdu"),
            ("Bilingual", "Bilingual"),
        ],
        default="English"
    )
    academic_year_start = models.DateField(blank=True, null=True)
    academic_year_end = models.DateField(blank=True, null=True)

    # Campus Mapping
    room_number = models.CharField(max_length=20, blank=True, null=True)

    # Administrative Info
    status = models.CharField(
        max_length=20,
        choices=[
            ("Active", "Active"),
            ("Inactive", "Inactive"),
            ("Temporary Closed", "Temporary Closed"),
        ],
        default="Active"
    )
    governing_body = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. Matric, Cambridge, IB"
    )

    # Extra notes
    description = models.TextField(blank=True, null=True, help_text="Optional notes about the section")

    def __str__(self):
        return f"{self.name} - {self.section} ({self.campus.name})"

    class Meta:
        unique_together = ("name", "section", "campus")
        ordering = ["name", "section"]
        verbose_name = "Class / Section"
        verbose_name_plural = "Classes / Sections"
