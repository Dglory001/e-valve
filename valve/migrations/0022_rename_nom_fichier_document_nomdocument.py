# Generated by Django 4.2.7 on 2024-02-21 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0021_remove_document_taille'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='nom_fichier',
            new_name='nomDocument',
        ),
    ]