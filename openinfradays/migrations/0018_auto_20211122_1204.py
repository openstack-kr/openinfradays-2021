# Generated by Django 3.2.9 on 2021-11-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0017_virtualbooth_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualbooth',
            name='custom_logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/virtualbooth/'),
        ),
        migrations.AlterField(
            model_name='virtualbooth',
            name='body',
            field=models.TextField(blank=True, default='', max_length=10000),
        ),
    ]