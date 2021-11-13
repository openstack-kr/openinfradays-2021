# Generated by Django 3.2.9 on 2021-11-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0012_techsession_qna_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techsession',
            old_name='slide_url',
            new_name='slide',
        ),
        migrations.AddField(
            model_name='techsession',
            name='open_date',
            field=models.DateField(choices=[('2021-12-07', '2021-12-07'), ('2021-12-08', '2021-12-08'), ('2021-12-09', '2021-12-09')], default='2021-12-07'),
        ),
    ]
