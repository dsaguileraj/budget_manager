# Generated by Django 5.0.7 on 2024-07-30 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=255)),
                ('cpc', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('activity', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('budget_type', models.CharField(choices=[('GC', 'Gasto Corriente'), ('PI', 'Proyecto de Inversión')], max_length=2)),
                ('bid', models.BooleanField(default=False)),
                ('c1', models.BooleanField(default=False)),
                ('c2', models.BooleanField(default=False)),
                ('c3', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['number', 'description', 'activity'],
                'unique_together': {('number', 'description', 'activity')},
            },
        ),
    ]
