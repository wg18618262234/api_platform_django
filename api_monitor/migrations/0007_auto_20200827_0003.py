# Generated by Django 3.1 on 2020-08-26 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_monitor', '0006_auto_20200827_0002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logs',
            new_name='RequestLog',
        ),
    ]