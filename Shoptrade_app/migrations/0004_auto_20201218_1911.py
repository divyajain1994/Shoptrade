# Generated by Django 3.1.2 on 2020-12-18 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shoptrade_app', '0003_auto_20201218_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer_name',
        ),
    ]
