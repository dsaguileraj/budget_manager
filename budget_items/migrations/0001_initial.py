# Generated by Django 5.0.3 on 2024-05-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255)),
                ('cpc', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('budget', models.FloatField()),
                ('budget_type', models.CharField(choices=[('Current Expense', 'Current Expense'), ('Investment Project', 'Investment Project')], max_length=18)),
                ('description', models.TextField()),
                ('activity', models.TextField()),
                ('bid', models.BooleanField()),
            ],
        ),
    ]
