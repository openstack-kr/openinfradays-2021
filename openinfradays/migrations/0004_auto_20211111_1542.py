# Generated by Django 3.2.9 on 2021-11-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0003_auto_20211111_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='homepage_url',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.CharField(choices=[('Diamond', 'Diamond'), ('Sapphire', 'Sapphire'), ('Gold', 'Gold')], default='Gold', max_length=20),
        ),
    ]
