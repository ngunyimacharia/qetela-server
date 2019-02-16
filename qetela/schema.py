import graphene
from organisations.schema import OrganisationQueries, OrganisationMutations

class Query(OrganisationQueries, graphene.ObjectType):
    pass


class Mutation(OrganisationMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
