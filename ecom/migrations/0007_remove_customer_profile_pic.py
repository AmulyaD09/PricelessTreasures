# Generated by Django 4.2.10 on 2024-02-20 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]