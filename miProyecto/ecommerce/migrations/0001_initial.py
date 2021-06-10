# Generated by Django 3.2.4 on 2021-06-04 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigoBarra', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50)),
                ('precioCosto', models.IntegerField()),
                ('precioVenta', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categoria')),
            ],
        ),
    ]
