from django.urls import path
from .views import register, home, vendor_dashboard, user_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('vendor-dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
]
