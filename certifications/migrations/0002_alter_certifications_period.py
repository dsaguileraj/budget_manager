# Generated by Django 5.0.3 on 2024-05-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='period',
            field=models.PositiveIntegerField(),
        ),
    ]