# Generated by Django 5.1.6 on 2025-03-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seances', '0003_alter_seance_statut'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance',
            name='places_reservees',
            field=models.IntegerField(default=0),
        ),
    ]
