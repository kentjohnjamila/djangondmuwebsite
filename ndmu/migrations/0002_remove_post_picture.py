# Generated by Django 2.1.3 on 2018-12-09 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]