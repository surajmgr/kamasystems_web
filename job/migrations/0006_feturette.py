# Generated by Django 2.2.4 on 2019-09-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20190905_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='feturette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1_title', models.CharField(max_length=200)),
                ('f1_stxt', models.CharField(blank=True, max_length=300)),
                ('f1_desc', models.TextField()),
                ('f1_img', models.ImageField(upload_to='media/images/featurette')),
                ('f2_title', models.CharField(max_length=200)),
                ('f2_stxt', models.CharField(blank=True, max_length=300)),
                ('f2_desc', models.TextField()),
                ('f2_img', models.ImageField(upload_to='media/images/featurette')),
                ('f3_title', models.CharField(max_length=200)),
                ('f3_stxt', models.CharField(blank=True, max_length=300)),
                ('f3_desc', models.TextField()),
                ('f3_img', models.ImageField(upload_to='media/images/featurette')),
            ],
        ),
    ]
