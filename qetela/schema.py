import graphene
from organisations.queries import OrganisationQueries
from organisations.mutations import OrganisationMutations

class Query(OrganisationQueries, graphene.ObjectType):
    pass


class Mutation(OrganisationMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
