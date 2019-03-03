from django.db import models

#model for chats
class Chat(models.Model):
    team = models.ForeignKey(
    'organisations.Team',
    on_delete=models.CASCADE,
    )
    goal = models.ForeignKey(
    'goals.Goal',
    on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated

class Message(models.Model):
    content = models.TextField()
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey('self', blank=True, null=True , on_delete=models.CASCADE, related_name='children')
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
    def __str__(self):
        return self.content[:10]
