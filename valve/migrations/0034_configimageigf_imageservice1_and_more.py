# Generated by Django 4.2.7 on 2024-02-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valve', '0033_configimageigf_imagesaft'),
    ]

    operations = [
        migrations.AddField(
            model_name='configimageigf',
            name='imageservice1',
            field=models.ImageField(blank=True, null=True, upload_to='configImage/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='configimageigf',
            name='imageservice2',
            field=models.ImageField(blank=True, null=True, upload_to='configImage/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='configimageigf',
            name='imageservice3',
            field=models.ImageField(blank=True, null=True, upload_to='configImage/%Y/%m/%d/'),
        ),
    ]
