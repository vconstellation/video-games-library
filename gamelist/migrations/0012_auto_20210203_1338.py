# Generated by Django 3.1.5 on 2021-02-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0011_auto_20210203_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescollection',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
