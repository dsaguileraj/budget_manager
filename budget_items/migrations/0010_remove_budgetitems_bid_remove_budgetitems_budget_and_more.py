# Generated by Django 5.0.3 on 2024-04-10 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_items', '0009_alter_budgetitems_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetitems',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='budget_type',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='cpc',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='date',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='description',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='number',
        ),
    ]