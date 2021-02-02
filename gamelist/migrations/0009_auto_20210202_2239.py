# Generated by Django 3.1.5 on 2021-02-02 21:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0008_auto_20210130_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescollection',
            name='cover',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_cover.jpg', force_format=None, keep_meta=True, quality=0, size=[300, 300], upload_to='game_cover'),
        ),
    ]
