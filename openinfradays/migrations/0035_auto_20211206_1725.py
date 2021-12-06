# Generated by Django 3.2.9 on 2021-12-06 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0034_auto_20211206_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimetoken',
            name='access_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='access_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 17, 25, 53, 100095)),
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 17, 25, 53, 99923)),
        ),
    ]
