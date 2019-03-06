from .models import Kit as KitModel
from .models import Task as TaskModel
from .models import Session as SessionModel
from .models import Progress as ProgressModel
from graphene_django.types import DjangoObjectType
import graphene

class Kit(DjangoObjectType):
    class Meta:
        model = KitModel


class Task(DjangoObjectType):
    class Meta:
        model = TaskModel

class Session(DjangoObjectType):
    class Meta:
        model = SessionModel

class Progress(DjangoObjectType):
    class Meta:
        model = ProgressModel

class OnboardingQueries(graphene.ObjectType):
    kit = graphene.Field(Kit,id=graphene.ID(required=True))
    kits = graphene.List(Kit)
    task = graphene.Field(Task,id=graphene.ID(required=True))
    tasks = graphene.List(Task)
    session = graphene.Field(Session,id=graphene.ID(required=True))
    sessions = graphene.List(Session)
    progress = graphene.Field(Progress,id=graphene.ID(required=True))
    progresses = graphene.List(Progress)

    def resolve_kit(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return KitModel.objects.get(pk=id)

    def resolve_kits(self, isfo, **kwargs):
        return KitModel.objects.all()

    def resolve_task(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TaskModel.objects.get(pk=id)

    def resolve_tasks(self, info, **kwargs):
        return TaskModel.objects.all()

    def resolve_session(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return SessionModel.objects.get(pk=id)

    def resolve_sessions(self, info, **kwargs):
        return SessionModel.objects.all()

    def resolve_progress(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ProgressModel.objects.get(pk=id)

    def resolve_progresses(self, info, **kwargs):
        return ProgressModel.objects.all()
