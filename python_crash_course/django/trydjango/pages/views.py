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
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 234, 3.14, 458, 505.50],
    }
    return render(request, 'about1.html', my_context)

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

