# Generated by Django 3.1.5 on 2021-02-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_profile_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='platform_used',
            field=models.TextField(max_length=30),
        ),
    ]