# Generated by Django 4.1.6 on 2023-03-14 04:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_alter_customer_options_remove_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"permissions": [("cancel_order", "Can change order")]},
        ),
    ]