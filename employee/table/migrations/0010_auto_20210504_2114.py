# Generated by Django 3.1.7 on 2021-05-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_auto_20210504_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='OfficeID',
            field=models.IntegerField(default=1),
        ),
    ]
