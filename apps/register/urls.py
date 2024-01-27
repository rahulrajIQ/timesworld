from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('failed', views.failed),
    path('login', views.login),
    path('login_page', views.login_page),
    path('dashboard', views.dashboard)
]