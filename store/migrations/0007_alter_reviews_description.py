# Generated by Django 4.2.8 on 2023-12-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
