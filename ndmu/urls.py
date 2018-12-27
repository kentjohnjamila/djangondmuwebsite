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
	path('about/vision-mission/', views.vision, name='ndmu-vision'),
	path('about/objectives/', views.objectives, name='ndmu-objectives'),
	path('about/core-values/', views.corevalues, name='ndmu-corevalues'),
	path('about/citation-and-awards/', views.citationsandawards, name='ndmu-citation'),
	path('about/core-values/', views.corevalues, name='ndmu-corevalues'),
	path('about/university-colors/', views.universitycolors, name='ndmu-colors'),
	path('about/university-hymn/', views.hymn, name='ndmu-hymn'),	
	path('about/university-seal/', views.seal, name='ndmu-seal'),
	path('about/marist-brothers/', views.maristbrothers, name='ndmu-brothers'),
	path('about/shs-strands/', views.strands, name='ndmu-strands'),
	path('about/school-facilities/', views.schoolfacilities, name='ndmu-facilities'),
    #########################################################################
    #announcements tab
	path('announcements/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('announcements/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('announcements/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('announcements/new/', PostCreateView.as_view(), name='post-create'),
    path('announcements/',  PostListView.as_view(), name='ndmu-announcements'),

    #########################################################################
    #user tag
	path('user/<username>/', UserPostListView.as_view(), name='user-posts'),
	#########################################################################
	#teacher tag
	path('shs-teachers/', views.teachers, name='ndmu-teachers'),
]
