# Generated by Django 4.2.7 on 2024-02-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0029_alter_document_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='document/%Y/%m/%d/'),
        ),
    ]
