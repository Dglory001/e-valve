# Generated by Django 4.2.6 on 2024-02-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0007_alter_document_concerne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='contenu',
            field=models.TextField(blank=True, null=True),
        ),
    ]
