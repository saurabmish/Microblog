from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='app-home'),
    path('about/', views.about, name='app-about'),
]
