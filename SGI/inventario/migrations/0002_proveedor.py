# Generated by Django 3.1.3 on 2023-04-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('cedula', models.CharField(max_length=1000000000, primary_key=True, serialize=False)),
                ('nombreproveedor', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=1000000)),
                ('telefono', models.CharField(max_length=1000000000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
