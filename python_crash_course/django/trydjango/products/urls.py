"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import sys
# sys.path.append("..")
from .views import (
    product_detail_view, product_create_view,
    product_post, dynamic_lookup_view, product_delete_view,
    product_list
)
# Sets the namespace for the products app
app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    # path('product_list/', product_list),
    path('<int:product_id>', dynamic_lookup_view, name='dynamic_lookup'),
    path('<int:product_id>/delete', product_delete_view,
         name='product_delete'),
    path('create/', product_create_view),
    path('post_request/', product_post),
]
