# Generated by Django 3.2.5 on 2021-08-06 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210806_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=django.utils.timezone.localtime),
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.TimeField(default=django.utils.timezone.localdate),
        ),
    ]
