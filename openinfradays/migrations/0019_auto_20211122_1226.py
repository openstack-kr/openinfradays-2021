# Generated by Django 3.2.9 on 2021-11-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0018_auto_20211122_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualbooth',
            name='link1_txt',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='virtualbooth',
            name='link2_txt',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='virtualbooth',
            name='link3_txt',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='virtualbooth',
            name='link4_txt',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='virtualbooth',
            name='link5_txt',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
