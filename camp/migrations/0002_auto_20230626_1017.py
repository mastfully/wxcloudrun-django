# Generated by Django 3.2.8 on 2023-06-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccamp',
            name='price',
            field=models.IntegerField(default=5980, verbose_name='价格'),
        ),
        migrations.AddField(
            model_name='jcamp',
            name='price',
            field=models.IntegerField(default=4980, verbose_name='价格'),
        ),
    ]
