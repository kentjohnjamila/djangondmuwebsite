# Generated by Django 2.1.3 on 2018-12-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0013_auto_20181210_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
