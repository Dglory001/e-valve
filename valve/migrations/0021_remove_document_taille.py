# Generated by Django 4.2.7 on 2024-02-21 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0020_alter_document_taille'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='taille',
        ),
    ]