from django.db import models
from campus.models import Campus
from teachers.models import Teacher
from students.models import Student


# --- Grade Model ---
class Grade(models.Model):
    GRADE_CHOICES = [
        ("Nursery", "Nursery"),
        ("KG1", "KG1"),
        ("KG2", "KG2"),
        ("1", "Grade 1"),
        ("2", "Grade 2"),
        ("3", "Grade 3"),
        ("4", "Grade 4"),
        ("5", "Grade 5"),
        ("6", "Grade 6"),
        ("7", "Grade 7"),
        ("8", "Grade 8"),
        ("9", "Grade 9"),
        ("10", "Grade 10"),
    ]

    name = models.CharField(max_length=20, choices=GRADE_CHOICES)
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name="grades"
    )
    capacity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("name", "campus")  # Prevent duplicate Grade per Campus
        ordering = ["campus", "name"]

    def __str__(self):
        return f"{self.name} - {self.campus.campus_name}"


# --- Section Model ---
class Section(models.Model):
    name = models.CharField(max_length=5)  # e.g., A, B, C
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    class_teacher = models.OneToOneField(  # one teacher → one section
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="class_section"
    )
    capacity = models.PositiveIntegerField(default=30)
    students = models.ManyToManyField(
        Student,
        blank=True,
        related_name="sections",
        help_text="Students enrolled in this section"
    )

    class Meta:
        unique_together = ("name", "grade")  # Prevent duplicate A/B per Grade
        ordering = ["grade", "name"]

    def __str__(self):
        return f"{self.grade.name} - {self.name} ({self.grade.campus.campus_name})"

    def add_student(self, student):
        """ Assign student if not already in another section of same grade """
        if self.students.filter(id=student.id).exists():
            return False  # Already in this section
        if Section.objects.filter(grade=self.grade, students=student).exists():
            return False  # Already assigned to another section of this grade
        if self.students.count() >= self.capacity:
            return False  # Section full
        self.students.add(student)
        return True


# --- ClassRoom Model (optional physical room) ---
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)  # e.g., Room 101
    section = models.OneToOneField(
        Section,
        on_delete=models.CASCADE,
        related_name="classroom"
    )
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.section}"
