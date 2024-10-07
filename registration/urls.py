from django.urls import path
from .views import user_login, register, dashboard, logout
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('success/', TemplateView.as_view(template_name="succcess_reg/succcess.html"), name='success'),
    path('', dashboard, name='dashboard'),
]
