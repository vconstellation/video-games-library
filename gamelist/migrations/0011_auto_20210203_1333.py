# Generated by Django 3.1.5 on 2021-02-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0010_auto_20210202_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_platform', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='gamescollection',
            name='platforms',
        ),
        migrations.AddField(
            model_name='gamescollection',
            name='game_platform',
            field=models.ManyToManyField(to='gamelist.GamePlatform'),
        ),
    ]
