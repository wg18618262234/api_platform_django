# Generated by Django 3.1 on 2020-08-26 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_monitor', '0007_auto_20200827_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlog',
            name='api_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_monitor.api'),
        ),
    ]
