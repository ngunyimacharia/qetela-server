# Generated by Django 2.1.5 on 2019-03-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20190303_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(default='Hello', max_length=200),
            preserve_default=False,
        ),
    ]