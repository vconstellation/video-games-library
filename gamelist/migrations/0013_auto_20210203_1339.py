# Generated by Django 3.1.5 on 2021-02-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0012_auto_20210203_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
