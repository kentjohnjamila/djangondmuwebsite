#####################################################################
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#####################################################################

#####################################################################
#announcements
def announcements(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'ndmu/announcements.html', context)

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
	fields = ['title', 'content', 'image_content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
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
	success_url = '/'

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
	return render(request, 'ndmu/history.html', {'title': 'History'})

def contact(request):
	return render(request, 'ndmu/contact.html')

def trustees(request):
	return render(request, 'ndmu/trustees.html', {'title': 'Board of Trustees'})

def administration(request):
	return render(request, 'ndmu/administration.html', {'title': 'Administration'})

def teachers(request):
	return render(request, 'ndmu/teachers.html', {'title': 'SHS teachers'})
####################################################################
#home
def home(request):
	return render(request, 'ndmu/home.html')


