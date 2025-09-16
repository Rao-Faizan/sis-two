# import graphene
# from students.schema import Query as StudentsQuery  
# import teachers.schema
# import campus.schema

# class Query(StudentsQuery, teachers.schema.Query, campus.schema.Query, graphene.ObjectType):
#     pass

# schema = graphene.Schema(query=Query)
 # testing/schema.py
import graphene
import students.schema
import teachers.schema
import campus.schema
import classes_section.schema

class Query(
    students.schema.Query,
    teachers.schema.Query,
    campus.schema.Query,
    classes_section.schema.Query,
    graphene.ObjectType,
):
    pass

class Mutation(
    students.schema.Mutation,
    teachers.schema.Mutation,
    campus.schema.Mutation,
    classes_section.schema.Mutation,
    graphene.ObjectType,
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
