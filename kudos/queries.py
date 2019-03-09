from .models import Kudo as KudoModel
from .models import Recommendation as RecommendationModel
from graphene_django.types import DjangoObjectType
import graphene

class Kudo(DjangoObjectType):
    class Meta:
        model = KudoModel


class Recommendation(DjangoObjectType):
    class Meta:
        model = RecommendationModel

class KudoQueries(graphene.ObjectType):
    kudo = graphene.Field(Kudo,id=graphene.ID(required=True))
    kudos = graphene.List(Kudo)
    recommendation = graphene.Field(Recommendation,id=graphene.ID(required=True))
    recommendations = graphene.List(Recommendation)

    def resolve_kudo(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KudoModel.objects.get(pk=id)

    def resolve_kudos(self, isfo, **kwargs):
        return RecommendationModel.objects.all()

    def resolve_recommendation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KudoModel.objects.get(pk=id)

    def resolve_recommendations(self, isfo, **kwargs):
        return RecommendationModel.objects.all()
