# Generated by Django 3.2.9 on 2021-11-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0020_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
