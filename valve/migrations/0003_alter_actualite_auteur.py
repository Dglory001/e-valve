# Generated by Django 4.2.6 on 2024-02-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0002_alter_actualite_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='auteur',
            field=models.CharField(blank=True, choices=[('IGF-CS', 'Chef de Service'), ('IGF-CSA', 'Chef de Service Adjoint'), ('COORDO', 'Coordonateur'), ('COORDA', 'Coordonateur Adjoint'), ('DIR', 'Directeur'), ('CD', 'Chef de Division'), ('CB', 'Chef de Bureau'), ('ASDIR', 'Assistant Directeur'), ('AUT', 'Autres')], max_length=250, null=True),
        ),
    ]
