# Generated by Django 3.2.8 on 2023-06-29 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0002_auto_20230626_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 9, 50, 53, 321220)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 9, 50, 53, 321246)),
        ),
    ]
