# Generated by Django 2.1.2 on 2018-10-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20181011_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='orderPrice',
            new_name='productPrice',
        ),
    ]
