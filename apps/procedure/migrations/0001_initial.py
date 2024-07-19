# Generated by Django 5.0.7 on 2024-07-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('regime', models.CharField(choices=[('C', 'Común'), ('E', 'Especial')], default=None, max_length=1, null=True)),
                ('product_type', models.CharField(choices=[('N', 'Normalizado'), ('!N', 'No Normalizado')], default=None, max_length=2, null=True)),
                ('purchase_type', models.CharField(choices=[('B', 'Bien'), ('C', 'Consultoría'), ('O', 'Obra'), ('S', 'Servicio')], max_length=1)),
            ],
            options={
                'ordering': ['name', 'purchase_type'],
                'unique_together': {('name', 'regime', 'product_type', 'purchase_type')},
            },
        ),
    ]
