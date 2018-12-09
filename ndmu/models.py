from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=100, default=False)
    #content = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imgs = models.ImageField(upload_to='imgs/%Y/%m/%d/', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})
