# Generated by Django 3.1 on 2020-08-26 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_monitor', '0003_auto_20200826_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitor',
            old_name='api_id',
            new_name='api',
        ),
    ]