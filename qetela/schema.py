import graphene
import graphql_jwt
from organisations.queries import OrganisationQueries
from organisations.mutations import OrganisationMutations
from accounts.queries import AccountQueries
from accounts.mutations import AccountMutations
from goals.queries import GoalQueries

class Query(OrganisationQueries, AccountQueries,GoalQueries, graphene.ObjectType):
    pass


class Mutation(OrganisationMutations, AccountMutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
