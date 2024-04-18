# Generated by Django 5.0.3 on 2024-04-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProceduresTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('regime', models.CharField(choices=[('Common', 'Common'), ('Special', 'Special'), ('Not Applicable', 'Not Applicable')], max_length=14)),
                ('product_type', models.CharField(choices=[('Normalized', 'Normalized'), ('Not Normalized', 'Not Normalized'), ('Not Applicable', 'Not Applicable')], max_length=14)),
                ('purchase_type', models.CharField(choices=[('Good', 'Good'), ('Service', 'Service'), ('Work', 'Work'), ('Consultancy', 'Consultancy'), ('Goods & Services', 'Goods & Services')], max_length=16)),
            ],
        ),
    ]
