#####################################################################
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters import rest_framework as filters
from django.db.models import Q
from django.shortcuts import redirect
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
import json
#####################################################################

#####################################################################
#announcements
class PostListView(ListView):
	model = Post
	template_name = 'ndmu/announcements.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'ndmu/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'ndmu/edit_post.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('ndmu-announcements')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

####################################################################
#about
def about(request):
	return render(request, 'ndmu/about.html')

def history(request):
	return render(request, 'ndmu/about/history.html', {'title': 'History'})

def contact(request):
	return render(request, 'ndmu/about/contact.html')

def trustees(request):
	return render(request, 'ndmu/about/trustees.html', {'title': 'Board of Trustees'})

def administration(request):
	return render(request, 'ndmu/about/administration.html', {'title': 'Administration'})

def teachers(request):
	return render(request, 'ndmu/about/teachers.html', {'title': 'SHS teachers'})

def vision(request):
	return render(request, 'ndmu/about/vision_mission.html', {'title': 'Vision & Mission'})

def objectives(request):
	return render(request, 'ndmu/about/objectives.html', {'title': 'Objectives'})

def corevalues(request):
	return render(request, 'ndmu/about/corevalues.html', {'title': 'Core Values'})

def citationsandawards(request):
	return render(request, 'ndmu/about/citationsandawards.html', {'title': 'Citations & Awards'})

def universitycolors(request):
	return render(request, 'ndmu/about/universitycolors.html', {'title': 'University Colors'})

def hymn(request):
	return render(request, 'ndmu/about/hymn.html', {'title': 'University Hymn'})

def seal(request):
	return render(request, 'ndmu/about/seal.html', {'title': 'University Seal'})

def maristbrothers(request):
	return render(request, 'ndmu/about/maristbrothers.html', {'title': 'The Marist Brothers'})

def strands(request):
	return render(request, 'ndmu/about/strands.html', {'title': 'Senior High School Strands'})

def schoolfacilities(request):
	return render(request, 'ndmu/about/schoolfacilities.html', {'title': 'School Facilities'})

####################################################################
#home
def home(request):
	return render(request, 'ndmu/home.html')

def superhome(request):
	return render(request, 'ndmu/superhomepage.html')
####################################################################\
def whatsnew(request):
	return render(request, 'ndmu/whats_new.html')