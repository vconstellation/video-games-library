# Generated by Django 3.1.5 on 2021-01-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0004_auto_20210118_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
