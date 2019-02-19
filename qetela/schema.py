import graphene
from organisations.queries import OrganisationQueries
from organisations.mutations import OrganisationMutations
from accounts.queries import AccountQueries
from accounts.mutations import AccountMutations

class Query(OrganisationQueries, AccountQueries, graphene.ObjectType):
    pass


class Mutation(OrganisationMutations, AccountMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
