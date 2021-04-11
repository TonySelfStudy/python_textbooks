from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(f'in pages.home_view()')
    print(request, args, kwargs)
    return render(request, 'home1.html', {})

def contact_view(request, *args, **kwargs):
    print(f'in pages.contact_view()')
    print(request, args, kwargs)
    return render(request, 'contact1.html', {})

def about_view(request, *args, **kwargs):
    print(f'in pages.about_view()')
    print(request, args, kwargs)
    return render(request, 'about1.html', {})

def social_view(request, *args, **kwargs):
    print(f'in pages.social_view()')
    print(request, args, kwargs)
    return render(request, 'social1.html', {})


def misc_view(request, *args, **kwargs):
    return_text = "<h1>Hello World</h1> <br>"
    print(request.GET)

    for arg in args:
        return_text += f'{arg}, '
    for k, v in kwargs.items():
        return_text += f'{k}: {v}, '

    return HttpResponse(return_text)

