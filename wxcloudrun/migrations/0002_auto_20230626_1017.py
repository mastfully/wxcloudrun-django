# Generated by Django 3.2.8 on 2023-06-26 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 10, 17, 27, 517571)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 10, 17, 27, 517597)),
        ),
    ]