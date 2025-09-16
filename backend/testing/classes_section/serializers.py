from rest_framework import serializers
from .models import Grade, Section
from teachers.models import TeacherRole
from campuses.models import Campus

# Teacher Serializer for nested info in Section
class TeacherRoleSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher.full_name", read_only=True)
    campus_name = serializers.CharField(source="campus.name", read_only=True)

    class Meta:
        model = TeacherRole
        fields = ["id", "teacher_name", "role_title", "campus_name"]

# Section Serializer
class SectionSerializer(serializers.ModelSerializer):
    grade_name = serializers.CharField(source="grade.name", read_only=True)
    campus_name = serializers.CharField(source="campus.name", read_only=True)
    class_teacher = TeacherRoleSerializer(read_only=True)  # Nested teacher info

    class Meta:
        model = Section
        fields = ["id", "name", "grade", "grade_name", "campus", "campus_name", "class_teacher"]

# Grade Serializer with nested sections
class GradeSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "name", "sections"]
