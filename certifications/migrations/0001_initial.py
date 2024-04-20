# Generated by Django 5.0.3 on 2024-04-19 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budget_items', '0001_initial'),
        ('departments', '0001_initial'),
        ('procedures_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('budget', models.FloatField()),
                ('description', models.TextField()),
                ('period', models.IntegerField()),
                ('budget_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget_items.budgetitems')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.departments')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedures_types.procedurestypes')),
            ],
        ),
    ]
