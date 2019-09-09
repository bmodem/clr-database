import graphene
from graphene_django.debug import DjangoDebug
from graphqlApp.schema import Query as bundle_query


class Query(bundle_query):
    debug = graphene.Field(DjangoDebug, name='_debug')
    pass


schema = graphene.Schema(query=Query, auto_camelcase=False)
