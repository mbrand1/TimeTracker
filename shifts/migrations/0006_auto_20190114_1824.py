# Generated by Django 2.1.5 on 2019-01-14 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_registration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'permissions': (('can_view_others', 'Can view others shifts and events'),)},
        ),
    ]