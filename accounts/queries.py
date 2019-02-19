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
    user = graphene.Field(User,username=graphene.String(required=True))

    def resolve_user(self, info, username):
        return UserModel.objects.get(username=username)

    def resolve_users(self, info,):
        return UserModel.objects.all()

    def resolve_user_positions(self, info):
        return UserPositionModel.objects.all()
