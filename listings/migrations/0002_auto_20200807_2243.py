# Generated by Django 2.0 on 2020-08-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing_model',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
