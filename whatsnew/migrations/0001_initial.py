# Generated by Django 2.1.3 on 2018-12-18 03:33

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Whatsnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsnew_title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=100)),
                ('whatsnew', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('new_imgs', models.ImageField(blank=True, max_length=255, null=True, upload_to='imgs/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]