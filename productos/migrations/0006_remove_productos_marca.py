# Generated by Django 4.2 on 2023-09-20 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0005_rename_producto_productos"),
    ]

    operations = [
        migrations.RemoveField(model_name="productos", name="marca",),
    ]
