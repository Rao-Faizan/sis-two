from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    campus = models.ForeignKey("campus.Campus", null=True, blank=True, on_delete=models.SET_NULL)
