# Generated by Django 3.2.9 on 2021-12-05 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0032_auto_20211204_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='techsession',
            name='ad1_url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='techsession',
            name='ad2_url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='access_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 4, 28, 48, 210471)),
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 4, 28, 48, 210265)),
        ),
    ]
