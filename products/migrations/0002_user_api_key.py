# Generated by Django 4.2.7 on 2024-06-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='api_key',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]