# Generated by Django 3.1.5 on 2021-01-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210112_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='steam_link',
            field=models.CharField(default='placeholder_url', max_length=20),
            preserve_default=False,
        ),
    ]
