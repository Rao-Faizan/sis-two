# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Grade, Section, ClassRoom
from .serializers import GradeSerializer, SectionSerializer, ClassRoomSerializer
from students.models import Student


# --- Grade ViewSet ---
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


# --- Section ViewSet ---
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    # ✅ Custom action: Get all students in this section
    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        section = self.get_object()
        students = section.students.all()
        return Response({"section": section.name, "students": [str(s) for s in students]})

    # ✅ Custom action: Assign student to section
    @action(detail=True, methods=["post"])
    def assign_student(self, request, pk=None):
        section = self.get_object()
        student_id = request.data.get("student_id")

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        # Check: student grade == section grade
        if student.grade != section.grade:
            return Response({"error": "Student not in this grade"}, status=400)

        # Check: already assigned to section
        if section.students.filter(id=student.id).exists():
            return Response({"error": "Student already in this section"}, status=400)

        section.students.add(student)
        return Response({"message": f"{student} assigned to {section}"})

    # ✅ Custom action: Remove student from section
    @action(detail=True, methods=["post"])
    def remove_student(self, request, pk=None):
        section = self.get_object()
        student_id = request.data.get("student_id")

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        if not section.students.filter(id=student.id).exists():
            return Response({"error": "Student not in this section"}, status=400)

        section.students.remove(student)
        return Response({"message": f"{student} removed from {section}"})


# --- ClassRoom ViewSet ---
class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
