# Generated by Django 4.1.5 on 2023-01-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
