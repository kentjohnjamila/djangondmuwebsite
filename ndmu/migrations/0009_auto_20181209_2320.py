# Generated by Django 2.1.3 on 2018-12-09 15:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0008_auto_20181209_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Description of the announcement.', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Type your title here.', max_length=100),
        ),
    ]
