# Generated by Django 3.1.5 on 2021-01-27 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0006_gamescollection_belong_to_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamescollection',
            name='developer',
        ),
    ]
