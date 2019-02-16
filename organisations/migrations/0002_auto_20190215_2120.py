# Generated by Django 2.1.5 on 2019-02-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='cf_frequency',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='website',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]
