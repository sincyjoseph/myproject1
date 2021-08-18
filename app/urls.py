from django.urls import path, include

from django.conf import settings
from app import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('sample', views.sample, name='sample'),
    path('index_save', views.index_save, name='index_save'),
]
