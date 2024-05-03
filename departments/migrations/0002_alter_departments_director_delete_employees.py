# Generated by Django 5.0.3 on 2024-05-03 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employees'),
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
