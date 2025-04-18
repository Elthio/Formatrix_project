# Generated by Django 5.1.6 on 2025-03-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('cours_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_cours', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('niveau', models.CharField(max_length=50, null=True)),
                ('frais_par_participant', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('duree_heures', models.IntegerField()),
                ('periode_mois', models.IntegerField(null=True)),
                ('type_cours', models.CharField(choices=[('formateur', 'Formation pour Formateur'), ('apprenant', 'Formation pour Apprenant'), ('court', 'Cours Court'), ('long', 'Cours Long')], max_length=50)),
                ('objectifs', models.TextField()),
                ('prerequis', models.TextField(null=True)),
                ('materiel_requis', models.TextField(null=True)),
                ('horaire', models.CharField(choices=[('pendant_bureau', 'Pendant les heures de bureau'), ('apres_bureau', 'Après les heures de bureau'), ('weekend', 'Weekend')], max_length=50)),
                ('statut_approbation', models.CharField(choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('refuse', 'Refusé'), ('expire', 'Expiré')], max_length=50)),
                ('date_approbation', models.DateField(null=True)),
                ('date_expiration_validite', models.DateField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cours',
            },
        ),
    ]
