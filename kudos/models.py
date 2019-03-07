from django.db import models

# model for kudos
class Kudo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sender = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    reciever = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='kudos_reciever_user'

    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
