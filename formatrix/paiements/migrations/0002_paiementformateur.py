# Generated by Django 5.1.6 on 2025-03-29 20:42

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formateurs', '0006_alter_formateur_adresse_and_more'),
        ('paiements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaiementFormateur',
            fields=[
                ('paiement_formateur_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateField(default=django.utils.timezone.now)),
                ('periode_debut', models.DateField(help_text='Début de la période de travail concernée par ce paiement')),
                ('periode_fin', models.DateField(help_text='Fin de la période de travail concernée par ce paiement')),
                ('statut', models.CharField(choices=[('paye', 'Payé'), ('en_attente', 'En attente'), ('planifie', 'Planifié'), ('annule', 'Annulé')], default='en_attente', max_length=20)),
                ('mode_paiement', models.CharField(choices=[('virement', 'Virement bancaire'), ('cheque', 'Chèque'), ('especes', 'Espèces'), ('autre', 'Autre')], default='virement', max_length=20)),
                ('reference', models.CharField(blank=True, help_text='Référence du paiement (ex: numéro de transaction)', max_length=100, null=True)),
                ('heures_travaillees', models.DecimalField(decimal_places=2, help_text="Nombre d'heures travaillées sur la période", max_digits=6)),
                ('taux_horaire', models.DecimalField(decimal_places=2, help_text='Taux horaire appliqué', max_digits=8)),
                ('commentaires', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('formateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiements', to='formateurs.formateur')),
            ],
            options={
                'verbose_name': 'Paiement Formateur',
                'verbose_name_plural': 'Paiements Formateurs',
                'ordering': ['-date_paiement'],
            },
        ),
    ]
