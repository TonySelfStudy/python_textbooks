
from django.urls import path, include
from .views import view_01

app_name = 'my_app_01'

urlpatterns = [
    path('', view_01, name='view_01a_str'),
    path('te', view_01, name='view_01b_str'),
    path('testy/', view_01, name='view_01c_str'),
    path('app_01/test/', view_01, name='view_01d_str'),
]
