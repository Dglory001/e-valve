# Generated by Django 4.2.7 on 2024-02-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0016_alter_configimageigf_imagepageigf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='categorie',
            field=models.CharField(blank=True, choices=[('AE', "Annonce d'un évenement"), ('CREV', "Compte rendu d'un évenement à venir"), ('CREP', "Compte rendu d'un évenement passé"), ('IEV', 'Invitation à un évenement'), ('AS', 'Avis de Sécurité'), ('ANP', "Annonce d'un nouveau programme"), ('AE', "Annonce d'un évenement")], max_length=255, null=True),
        ),
    ]
