from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth.urls import views as auth_views


urlpatterns=[
    path('', views.home, name='layout-home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('profile_update/', user_views.profile_update, name='profile-update')
]