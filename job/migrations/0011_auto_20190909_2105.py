# Generated by Django 2.2.4 on 2019-09-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20190909_1908'),
    ]

    operations = [
        migrations.DeleteModel(
            name='job',
        ),
        migrations.AlterField(
            model_name='featurette',
            name='f1_img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='featurette',
            name='f2_img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='featurette',
            name='f3_img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='topprojects',
            name='icon',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
