from .models import Chat as ChatModel
from .models import Message as MessageModel
from graphene_django.types import DjangoObjectType
import graphene

class Chat(DjangoObjectType):
    class Meta:
        model = ChatModel

class Message(DjangoObjectType):
    class Meta:
        model = MessageModel

class ChatQueries(graphene.ObjectType):
    chat = graphene.Field(Chat,id=graphene.ID(required=True))
    chats = graphene.List(Chat)
    message = graphene.Field(Message,id=graphene.ID(required=True))
    messages = graphene.List(Message)

    def resolve_chat(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ChatModel.objects.get(pk=id)
        return None

    def resolve_chats(self, info, **kwargs):
        return ChatModel.objects.all()

    def resolve_message(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return MessageModel.objects.get(pk=id)
        return None

    def resolve_messages(self, info, **kwargs):
        return MessageModel.objects.all()
