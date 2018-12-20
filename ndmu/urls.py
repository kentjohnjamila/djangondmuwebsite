#####################################################################
from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.views.generic.base import RedirectView
#####################################################################

urlpatterns = [
	#home tab
	path('home/', views.home, name='ndmu-home'),
	path('', views.superhome, name="ndmu-superhome"),
	#########################################################################
	#about tab
    path('about/', views.about, name='ndmu-about'),
	path('about/history/', views.history, name='ndmu-history'),
	path('about/contact/', views.contact, name='ndmu-contact'),
	path('about/board-of-trustees/', views.trustees, name='ndmu-trustees'),
	path('about/administration/', views.administration, name='ndmu-administration'),
    #########################################################################
    #announcements tab
	path('announcements/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('announcements/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('announcements/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('announcements/new/', PostCreateView.as_view(), name='post-create'),
    path('announcements/',  PostListView.as_view(), name='ndmu-announcements'),

    #########################################################################
    #user tag
	path('user/<username>', UserPostListView.as_view(), name='user-posts'),
	#########################################################################
	#teacher tag
	path('shs-teachers/', views.teachers, name='ndmu-teachers'),
]
