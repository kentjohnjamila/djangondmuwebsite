# Generated by Django 2.1.3 on 2018-12-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0002_post_image_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_content',
            field=models.FileField(blank=True, null=True, upload_to='content_images'),
        ),
    ]
