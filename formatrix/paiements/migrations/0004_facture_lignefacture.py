# Generated by Django 5.1.6 on 2025-03-30 08:49

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0002_alter_inscription_unique_together_and_more'),
        ('paiements', '0003_delete_rappel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('facture_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero_facture', models.CharField(blank=True, max_length=20, unique=True)),
                ('type_facture', models.CharField(choices=[('individuelle', 'Individuelle'), ('entreprise', 'Entreprise'), ('sponsor', 'Sponsor')], default='individuelle', max_length=20)),
                ('statut', models.CharField(choices=[('brouillon', 'Brouillon'), ('emise', 'Émise'), ('payee', 'Payée'), ('annulee', 'Annulée')], default='brouillon', max_length=20)),
                ('date_emission', models.DateField(default=django.utils.timezone.now)),
                ('date_echeance', models.DateField(blank=True, null=True)),
                ('montant_ht', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('taux_tva', models.DecimalField(decimal_places=2, default=20.0, max_digits=5)),
                ('montant_tva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('montant_ttc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('destinataire_nom', models.CharField(max_length=255)),
                ('destinataire_adresse', models.TextField()),
                ('destinataire_email', models.EmailField(max_length=254)),
                ('destinataire_telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('destinataire_siret', models.CharField(blank=True, max_length=14, null=True)),
                ('conditions_paiement', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('inscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factures', to='inscriptions.inscription')),
                ('paiement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factures', to='paiements.paiement')),
            ],
            options={
                'verbose_name': 'Facture',
                'verbose_name_plural': 'Factures',
                'ordering': ['-date_emission'],
            },
        ),
        migrations.CreateModel(
            name='LigneFacture',
            fields=[
                ('ligne_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('quantite', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('prix_unitaire_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taux_tva', models.DecimalField(decimal_places=2, default=20.0, max_digits=5)),
                ('montant_tva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_ttc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='paiements.facture')),
            ],
            options={
                'verbose_name': 'Ligne de facture',
                'verbose_name_plural': 'Lignes de facture',
            },
        ),
    ]
