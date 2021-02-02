# Generated by Django 3.1.5 on 2021-02-02 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profile_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_type', models.CharField(max_length=10)),
                ('gpu', models.CharField(max_length=12)),
                ('gpu_memory', models.CharField(max_length=6)),
                ('cpu', models.CharField(max_length=10)),
                ('cpu_speed', models.CharField(max_length=6)),
                ('power_supply', models.CharField(max_length=12)),
                ('storage', models.CharField(max_length=20)),
                ('memory', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='hardware',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profilehardware'),
        ),
    ]