# Generated by Django 4.2.7 on 2024-03-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0050_configimageblog1_delete_configimageblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configimageblog1',
            name='parablog1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='configimageblog1',
            name='titreblog1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]