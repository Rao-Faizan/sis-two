from django.urls import path
from .views import GradeListView, SectionListView

urlpatterns = [
    path("grades/", GradeListView.as_view(), name="grades-list"),
    path("sections/", SectionListView.as_view(), name="sections-list"),
]
