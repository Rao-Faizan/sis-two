import graphene
from graphene_django import DjangoObjectType
from .models import Grade

class GradeType(DjangoObjectType):
    class Meta:
        model = Grade
        fields = "__all__"

class Query(graphene.ObjectType):
    all_grades = graphene.List(GradeType)

    def resolve_all_grades(root, info):
        return Grade.objects.all()
class Mutation(graphene.ObjectType):
    # agar abhi mutation nahi banana to pass rakho
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
