# Generated by Django 5.1.6 on 2025-03-05 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evaluations', '0001_initial'),
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultat',
            name='inscription',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inscriptions.inscription'),
        ),
    ]
