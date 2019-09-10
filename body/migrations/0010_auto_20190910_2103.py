# Generated by Django 2.2.4 on 2019-09-10 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0009_auto_20190910_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-pub_date']},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
