# Generated by Django 2.2.6 on 2020-10-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Address',
            new_name='address',
        ),
    ]
