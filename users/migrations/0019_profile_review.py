# Generated by Django 3.1.5 on 2021-02-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0010_auto_20210202_2244'),
        ('users', '0018_remove_profile_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='review',
            field=models.ManyToManyField(to='gamelist.GamesReviews'),
        ),
    ]
