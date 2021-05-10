from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schoolyears/', views.schoolyears, name='schoolyears'),
    path('projects/', views.projects, name='projects'),
    path('users/', views.users, name='users')
]
