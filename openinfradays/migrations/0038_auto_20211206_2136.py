# Generated by Django 3.2.9 on 2021-12-06 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0037_auto_20211206_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='access_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 21, 36, 33, 307320)),
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 21, 36, 33, 307129)),
        ),
    ]
