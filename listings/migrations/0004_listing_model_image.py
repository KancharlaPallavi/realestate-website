# Generated by Django 3.1 on 2020-08-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_listing_model_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing_model',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
