# Generated by Django 5.1.6 on 2025-03-04 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_module', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duree_heures', models.IntegerField()),
                ('ordre', models.IntegerField()),
                ('objectifs_module', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.cours')),
            ],
            options={
                'db_table': 'module',
            },
        ),
    ]
