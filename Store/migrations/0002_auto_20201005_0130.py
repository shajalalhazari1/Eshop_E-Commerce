# Generated by Django 3.0 on 2020-10-04 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discount_price',
            new_name='old_price',
        ),
    ]
