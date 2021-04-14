from django.shortcuts import render

# Create your views here.
def view_02(request):
    print('in view_02')
    my_data = {'view_func_name': 'view_02'}
    context = {
        'object': my_data
    }
    return render(request, 'app_02/file_02.html', context)
