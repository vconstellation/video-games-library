# Generated by Django 3.1.5 on 2021-01-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0004_auto_20210118_1948'),
        ('users', '0006_auto_20210124_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='game',
            field=models.ManyToManyField(through='users.ProfileGamesCollection', to='gamelist.GamesCollection'),
        ),
    ]
