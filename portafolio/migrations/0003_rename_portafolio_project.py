# Generated by Django 4.2 on 2023-08-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0002_category_portafolio_delete_project"),
    ]

    operations = [
        migrations.RenameModel(old_name="portafolio", new_name="project",),
    ]