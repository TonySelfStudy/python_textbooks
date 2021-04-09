from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    # return 'dollar dollar bill yo!'
    # return render(request, 'learning_logs/topics2.html')
    # return render(request, 'learning_logs/topics2.html', context)
    return render(request, 'learning_logs/topics.html', context)
