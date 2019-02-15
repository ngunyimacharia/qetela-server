from organisations.models import Organisation as OrganisationModel
from graphene_django.types import DjangoObjectType
import graphene

class Organisation(DjangoObjectType):
    class Meta:
        model = OrganisationModel


class Query(graphene.ObjectType):
    organisations = graphene.List(Organisation)

    def resolve_organisations(self, info):
        return OrganisationModel.objects.all()

schema = graphene.Schema(query=Query)
