from organisations.models import Organisation as OrganisationModel
from organisations.models import Level as LevelModel
from organisations.models import Team as TeamModel
from graphene_django.types import DjangoObjectType
import graphene

class Organisation(DjangoObjectType):
    class Meta:
        model = OrganisationModel

class Level(DjangoObjectType):
    class Meta:
        model = LevelModel

class Team(DjangoObjectType):
    class Meta:
        model = TeamModel

class OrganisationQueries(graphene.ObjectType):
    organisation = graphene.Field(Organisation,id=graphene.ID(required=True))
    organisations = graphene.List(Organisation)

    def resolve_organisation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return OrganisationModel.objects.get(pk=id)
        return None

    def resolve_organisations(self, info, **kwargs):
        return OrganisationModel.objects.all()

    def resolve_levels(self, info, **kwargs):
        return LevelModel.objects.all()

    def resolve_teams(self, info, **kwargs):
        return TeamModel.objects.all()
