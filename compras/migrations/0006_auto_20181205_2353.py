# Generated by Django 2.1.2 on 2018-12-06 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_producto_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]
