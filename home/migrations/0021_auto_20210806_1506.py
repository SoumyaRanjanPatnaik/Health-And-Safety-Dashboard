# Generated by Django 3.2.5 on 2021-08-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20210806_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
