from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return_text = "<h1>Hello World</h1> <br>"
    for arg in args:
        return_text += f'{arg}, '
    for k, v in kwargs.items():
        return_text += f'{k}: {v}, '

    return HttpResponse(return_text)
