# Generated by Django 3.1.3 on 2023-04-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_factura'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedora',
            fields=[
                ('id', models.CharField(max_length=1000000000, primary_key=True, serialize=False)),
                ('nombreproveedora', models.CharField(max_length=100)),
                ('direcciones', models.CharField(max_length=1000000)),
                ('contacto', models.CharField(max_length=1000000000)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
