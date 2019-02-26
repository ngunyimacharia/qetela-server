from django.contrib.auth.models import User as UserModel
from graphene_django.types import DjangoObjectType
from random import randint
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
    random_user = graphene.Field(User)

    def resolve_user(self, info, email):
        return UserModel.objects.get(email=email)

    def resolve_random_user(self, info,):
        count = UserModel.objects.count()
        random_index = randint(0, count - 1)
        return UserModel.objects.all()[random_index]

    def resolve_users(self, info,):
        return UserModel.objects.all()

    def resolve_user_positions(self, info):
        return UserPositionModel.objects.all()
