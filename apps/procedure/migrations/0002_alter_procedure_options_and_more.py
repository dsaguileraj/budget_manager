# Generated by Django 5.0.7 on 2024-07-29 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procedure',
            options={'ordering': ['name', 'purchase_type', 'product_type', 'regime']},
        ),
        migrations.AlterUniqueTogether(
            name='procedure',
            unique_together={('name', 'purchase_type', 'product_type', 'regime')},
        ),
    ]
