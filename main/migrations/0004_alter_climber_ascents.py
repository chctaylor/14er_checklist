# Generated by Django 3.2.5 on 2021-07-15 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210715_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climber',
            name='ascents',
            field=models.ManyToManyField(related_name='climber', to='main.Mountain'),
        ),
    ]
