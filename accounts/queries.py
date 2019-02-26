from django.contrib.auth.models import User as UserModel
from .models import UserPosition as UserPositionModel
import graphene
from graphene_django_extras import  DjangoFilterPaginateListField, LimitOffsetGraphqlPagination, DjangoObjectType

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        filter_fields = {
            'id': ['exact', ],
            'first_name': ['icontains', 'iexact'],
            'last_name': ['icontains', 'iexact'],
            'username': ['icontains', 'iexact'],
            'email': ['icontains', 'iexact']
        }

class UserPosition(DjangoObjectType):
    class Meta:
        model = UserPositionModel

class AccountQueries(graphene.ObjectType):
    users = DjangoFilterPaginateListField(User, pagination=LimitOffsetGraphqlPagination())
    user = graphene.Field(User,email=graphene.String(required=True))

    def resolve_user(self, info, email):
        return UserModel.objects.get(email=email)

    def resolve_user_positions(self, info):
        return UserPositionModel.objects.all()
