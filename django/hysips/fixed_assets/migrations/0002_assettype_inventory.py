# Generated by Django 3.2 on 2021-04-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assettype',
            name='inventory',
            field=models.BooleanField(default=True),
        ),
    ]