from django.contrib.auth.models import User as UserModel
from graphene_django.types import DjangoObjectType
from .models import UserPosition as UserPositionModel
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class UserPosition(DjangoObjectType):
    class Meta:
        model = UserPositionModel

class AccountQueries(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User,email=graphene.String(required=True))

    def resolve_user(self, info, email):
        return UserModel.objects.get(email=email)

    def resolve_users(self, info,):
        return UserModel.objects.all()

    def resolve_user_positions(self, info):
        return UserPositionModel.objects.all()
