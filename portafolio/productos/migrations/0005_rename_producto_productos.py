# Generated by Django 4.2.1 on 2023-09-13 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_category_producto_delete_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='producto',
            new_name='productos',
        ),
    ]
