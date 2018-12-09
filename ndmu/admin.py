from django.contrib import admin
from .models import Post
from django.urls import path
from django.http import HttpResponseRedirect

admin.site.site_header = 'NDMU Admin Page'
admin.site.site_title = 'NDMU Admin Page'

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content')
	list_filter = ('date_posted',)

admin.site.register(Post, PostAdmin)