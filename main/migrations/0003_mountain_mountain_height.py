# Generated by Django 3.2.5 on 2021-07-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mountain_mountain_climbed'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='mountain_height',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
