# Generated by Django 3.2.4 on 2021-06-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=80)),
                ('fechanac', models.DateField()),
                ('telefono', models.IntegerField()),
                ('pais', models.CharField(max_length=20)),
                ('niveleduc', models.CharField(max_length=20)),
            ],
        ),
    ]
