# Generated by Django 2.2.4 on 2019-09-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(help_text='Write your message here...', max_length=2000),
        ),
    ]