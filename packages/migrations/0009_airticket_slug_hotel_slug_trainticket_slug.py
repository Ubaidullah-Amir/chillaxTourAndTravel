# Generated by Django 4.0.3 on 2023-01-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0008_remove_hotel_currency_alter_hotel_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airticket',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='trainticket',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
