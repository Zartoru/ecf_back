from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schoolyears/', views.schoolyears, name='schoolyears',)
]
