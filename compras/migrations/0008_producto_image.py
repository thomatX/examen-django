# Generated by Django 2.1.2 on 2018-12-06 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20181205_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(default='products/default.png', upload_to='products/'),
        ),
    ]
