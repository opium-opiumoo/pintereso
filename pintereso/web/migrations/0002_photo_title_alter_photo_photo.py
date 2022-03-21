# Generated by Django 4.0.2 on 2022-03-21 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default=1, max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
