from django.urls import path
from . import views

app_name = 'pandeyfamily'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('video/', views.video, name='video'),
    path('kuldevta/', views.kuldevta, name='kuldevta'),
    path('vanshavali/', views.vanshavali, name='vanshavali'),

]
