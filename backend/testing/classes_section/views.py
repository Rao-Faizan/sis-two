from rest_framework import generics
from .models import Grade, Section
from .serializers import GradeSerializer, SectionSerializer

# List all grades with nested sections
class GradeListView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

# List all sections
class SectionListView(generics.ListAPIView):
    queryset = Section.objects.select_related("grade", "campus", "class_teacher").all()
    serializer_class = SectionSerializer
