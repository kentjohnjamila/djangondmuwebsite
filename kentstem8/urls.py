###################################################
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from ndmu import views as chat_views
from whatsnew import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
####################################################


urlpatterns = [
	path('whats-new/update/', views.WNewCreateView.as_view(), name="create-new"),
	path('whats-new/', views.WNewListView.as_view(), name='new-view'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/update/', user_views.profileedit, name='updateprofile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('ndmu.urls')),
    #########################################################################
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)