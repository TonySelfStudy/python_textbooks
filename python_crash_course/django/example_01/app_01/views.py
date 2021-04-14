from django.shortcuts import render, redirect, HttpResponse
import datetime


# Create your views here.
def view_01(request):
    print('in view_01')
    my_data = {'view_func_name': 'view_01',
               'time_of_day': str(datetime.datetime.now())}

    context = {
        'object': my_data
    }
    return render(request, 'app_01/file_01.html', context)
