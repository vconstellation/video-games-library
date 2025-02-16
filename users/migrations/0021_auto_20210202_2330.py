# Generated by Django 3.1.5 on 2021-02-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210202_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='platform_used',
        ),
        migrations.AddField(
            model_name='profile',
            name='platform_used',
            field=models.ManyToManyField(to='users.Platform'),
        ),
    ]
