# Generated by Django 4.1.6 on 2023-02-14 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='place_at',
            new_name='placed_at',
        ),
    ]
