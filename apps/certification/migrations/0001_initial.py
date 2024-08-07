# Generated by Django 5.0.7 on 2024-07-26 19:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budget_item', '0001_initial'),
        ('department', '0001_initial'),
        ('procedure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('budget', models.DecimalField(decimal_places=5, default=0, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('budget_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget_item.budgetitem')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.department')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='procedure.procedure')),
            ],
            options={
                'ordering': ['number', 'budget_item', 'description'],
                'unique_together': {('number', 'budget_item')},
            },
        ),
    ]
