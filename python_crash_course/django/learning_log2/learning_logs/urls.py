# learning_logs\urls.py

from django.urls import path, include
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='index'),
]
