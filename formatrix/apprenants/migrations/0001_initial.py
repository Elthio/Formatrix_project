# Generated by Django 5.1.6 on 2025-03-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('apprenant_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_apprenant', models.CharField(max_length=100)),
                ('autres_nom', models.CharField(blank=True, max_length=100, null=True)),
                ('cin', models.CharField(max_length=20, unique=True)),
                ('date_naissance', models.DateField()),
                ('adresse_rue', models.TextField()),
                ('localite', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('type_apprenant', models.CharField(blank=True, max_length=50, null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin'), ('A', 'Autre')], max_length=1)),
                ('niveau_academique', models.CharField(choices=[('sous_certificat', 'En dessous du certificat scolaire'), ('certificat', 'Certificat scolaire'), ('superieur', 'Au-dessus du certificat')], max_length=50)),
                ('categorie_age', models.CharField(choices=[('16-30', '16-30 ans'), ('31-60', '31-60 ans'), ('60+', 'Plus de 60 ans')], max_length=20)),
                ('besoins_speciaux', models.TextField(blank=True, null=True)),
                ('contact_urgence', models.CharField(max_length=100)),
                ('telephone_urgence', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'apprenant',
            },
        ),
    ]
