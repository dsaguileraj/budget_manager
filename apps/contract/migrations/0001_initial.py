# Generated by Django 5.0.7 on 2024-07-31 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certification', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=30, unique=True)),
                ('contractor', models.CharField(max_length=100)),
                ('suscription', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.employee')),
                ('certification', models.ManyToManyField(to='certification.certification')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
