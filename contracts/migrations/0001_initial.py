# Generated by Django 5.0.3 on 2024-05-03 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certifications', '0002_alter_certifications_period'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('advance', models.BooleanField(default=False)),
                ('contractor', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employees')),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='certifications.certifications')),
            ],
        ),
    ]
