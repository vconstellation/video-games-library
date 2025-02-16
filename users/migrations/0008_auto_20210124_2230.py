# Generated by Django 3.1.5 on 2021-01-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilegamescollection',
            name='currently_playing',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilegamescollection',
            name='finished',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
