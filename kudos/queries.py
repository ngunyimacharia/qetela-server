from .models import Kudo as KudoModel
from graphene_django.types import DjangoObjectType
import graphene

class Kudo(DjangoObjectType):
    class Meta:
        model = KudoModel

class KudoQueries(graphene.ObjectType):
    kudo = graphene.Field(Kudo,id=graphene.ID(required=True))
    kudos = graphene.List(Kudo)

    def resolve_kudo(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KudoModel.objects.get(pk=id)

    def resolve_kudos(self, isfo, **kwargs):
        return KudoModel.objects.all()
