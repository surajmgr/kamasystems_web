# Generated by Django 2.2.4 on 2019-09-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0007_auto_20190909_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='icon',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='ss1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='ss2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='ss3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='ss4',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]