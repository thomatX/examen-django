# Generated by Django 2.1.2 on 2018-12-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_auto_20181205_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]