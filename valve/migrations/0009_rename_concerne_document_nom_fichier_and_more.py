# Generated by Django 4.2.6 on 2024-02-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0008_alter_actualite_contenu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='concerne',
            new_name='nom_fichier',
        ),
        migrations.AlterField(
            model_name='document',
            name='fichier',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
