# Generated by Django 3.1.7 on 2021-05-05 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_auto_20210504_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='OfficeID',
        ),
    ]