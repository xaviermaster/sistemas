# Generated by Django 3.0.7 on 2020-07-14 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200713_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='enlace',
        ),
    ]
