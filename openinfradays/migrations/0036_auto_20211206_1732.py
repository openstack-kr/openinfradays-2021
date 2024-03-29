# Generated by Django 3.2.9 on 2021-12-06 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0035_auto_20211206_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimetoken',
            name='error_msg',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='access_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 17, 32, 56, 857662)),
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 17, 32, 56, 857482)),
        ),
    ]
