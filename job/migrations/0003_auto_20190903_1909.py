# Generated by Django 2.2.4 on 2019-09-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20190902_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
