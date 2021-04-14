
from django.urls import path, include
from .views import view_02

app_name = 'my_app_02'

urlpatterns = [
    path('', view_02, name='view_02a_str'),
    path('test', view_02, name='view_02b_str'),
]
