from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'imgs']


class UserAnnouncementForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

