# Generated by Django 3.1.7 on 2021-05-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0008_auto_20210504_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='OTP',
        ),
        migrations.AlterField(
            model_name='employee',
            name='OfficeID',
            field=models.IntegerField(),
        ),
    ]
