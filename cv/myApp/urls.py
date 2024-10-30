from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pengalaman/', views.pengalaman, name='pengalaman'),
    path('sosialmedia/', views.sosialmedia, name='sosialmedia'),
]