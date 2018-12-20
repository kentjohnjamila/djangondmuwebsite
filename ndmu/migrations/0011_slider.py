# Generated by Django 2.1.3 on 2018-12-10 11:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0010_auto_20181209_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_title', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True)),
                ('slide_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='slide_images/%Y/%m/%d/')),
            ],
        ),
    ]