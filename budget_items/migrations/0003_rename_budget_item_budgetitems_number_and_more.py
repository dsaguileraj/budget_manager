# Generated by Django 5.0.3 on 2024-04-06 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_items', '0002_budgetitems_departments_procedurestypes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budgetitems',
            old_name='budget_item',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='certifications',
            old_name='budget_item_reference',
            new_name='budget_item',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='name',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='purchase_type',
        ),
        migrations.RemoveField(
            model_name='budgetitems',
            name='regime',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='budget_type',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='cpc',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='purchase_type',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='regime',
        ),
        migrations.AlterField(
            model_name='certifications',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget_items.departments'),
        ),
        migrations.AlterField(
            model_name='certifications',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget_items.procedurestypes'),
        ),
    ]
