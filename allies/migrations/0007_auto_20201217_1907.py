# Generated by Django 3.1 on 2020-12-18 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allies', '0006_auto_20201215_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ally',
            new_name='CurrentAlly',
        ),
    ]
