# Generated by Django 2.1.5 on 2019-03-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_goalallocation_kpi_kpiupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='change',
            field=models.CharField(choices=[('>', 'Increase'), ('=', 'Equals'), ('<', 'Decrease')], default='=', max_length=1),
        ),
    ]
