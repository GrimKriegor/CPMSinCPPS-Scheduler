# Generated by Django 2.0.6 on 2018-06-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0002_auto_20180621_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledactivity',
            name='end_datetime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scheduledactivity',
            name='start_datetime',
            field=models.CharField(max_length=100),
        ),
    ]