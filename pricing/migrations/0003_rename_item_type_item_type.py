# Generated by Django 4.2.10 on 2024-02-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_rename_type_item_item_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_type',
            new_name='type',
        ),
    ]
