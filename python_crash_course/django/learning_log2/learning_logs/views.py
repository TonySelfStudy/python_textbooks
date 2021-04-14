from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Entry


# Create your views here.
def index(request):
    print(f'in index()')
    return render(request, "learning_logs/index.html")


def topics(request):
    print(f'in topics()')
    queryset = Topic.objects.all()

    context = {
        "topics": queryset
    }
    return render(request, "learning_logs/topics.html", context)
