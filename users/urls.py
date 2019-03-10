from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, view_profile, edit_profile
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit_profile, name='edit_profile'),
    path('view', view_profile, name='view_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
]