# Generated by Django 5.0.3 on 2024-04-17 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitems',
            name='budget_type',
            field=models.CharField(choices=[('Current Expense', 'Current Expense'), ('Investment Project', 'Investment Project')], max_length=18),
        ),
    ]
