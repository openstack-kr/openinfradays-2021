# Generated by Django 3.2.9 on 2021-12-04 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0031_auto_20211204_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='bof',
            name='profile_img',
            field=models.ImageField(blank=True, default=None, upload_to='images/bof/'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='access_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 16, 17, 22, 920402)),
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 16, 17, 22, 920232)),
        ),
    ]
