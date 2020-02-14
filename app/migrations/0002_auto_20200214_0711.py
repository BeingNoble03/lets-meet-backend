# Generated by Django 3.0.3 on 2020-02-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='date_and_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]