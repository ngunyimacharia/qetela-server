# Generated by Django 2.1.5 on 2019-03-09 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20190309_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpiupdate',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
