# Generated by Django 4.0.2 on 2022-03-21 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_photo_title_alter_photo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
    ]
