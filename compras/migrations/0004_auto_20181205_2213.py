# Generated by Django 2.1.2 on 2018-12-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_lista_producto_productocliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.AlterField(
            model_name='producto',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
