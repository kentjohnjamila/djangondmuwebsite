# Generated by Django 2.1.3 on 2018-12-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0006_auto_20181209_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
