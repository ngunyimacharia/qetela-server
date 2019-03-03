from goals.models import Goal as GoalModel
from goals.models import GoalAllocation as GoalAllocationModel
from goals.models import Kpi as KpiModel
from goals.models import KpiUpdate as KpiUpdateModel
from graphene_django.types import DjangoObjectType
import graphene

class Goal(DjangoObjectType):
    class Meta:
        model = GoalModel

class GoalAllocation(DjangoObjectType):
    class Meta:
        model = GoalAllocationModel

class Kpi(DjangoObjectType):
    class Meta:
        model = KpiModel

class KpiUpdate(DjangoObjectType):
    class Meta:
        model = KpiUpdateModel

class OrganisationQueries(graphene.ObjectType):
    goal = graphene.Field(Goal,id=graphene.ID(required=True))
    goals = graphene.List(Goals)

    def resolve_goal(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return GoalModel.objects.get(pk=id)
        return None

    def resolve_goals(self, info, **kwargs):
        return GoalModel.objects.all()

    def resolve_goal_allocation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return GoalAllocationModel.objects.get(pk=id)
        return None

    def resolve_goal_allocations(self, info, **kwargs):
        return GoalAllocationModel.objects.all()

    def resolve_kpi(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KpiModel.objects.get(pk=id)
        return None

    def resolve_kpis(self, info, **kwargs):
        return KpiModel.objects.all()


    def resolve_kpi_update(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KpiUpdateModel.objects.get(pk=id)
        return None

    def resolve_kpis(self,info,**kwargs):
        return KpisModel.objects.all()
