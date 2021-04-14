from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    print(f'in index()')
    return render(request, "learning_logs/index.html")


def view_topics(request):
    print(f'in view_topics()')
    # queryset = Topic.objects.all()
    queryset = Topic.objects.order_by('date_added')

    context = {
        "topics": queryset
    }
    return render(request, "learning_logs/topics.html", context)

def view_topic(request, topic_id):
    print(f'in view_topic()')

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {
        "topic": topic,
        "entries": entries
    }
    return render(request, "learning_logs/topic.html", context)


def create_topic(request):
    print(f'in create_topic()')
    print(f'{request.method=}')

    if request.method == 'POST':
        print(f'processing post request')
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:view_topics')
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = TopicForm()

    # Display blank or invalid form
    context = {
        "form": form,
    }
    return render(request, "learning_logs/create_topic.html", context)


def create_entry(request, topic_id=0):
    # topic_id is used to set the initial state of the topic combo box

    print(f'in create_entry()')
    print(f'{request.method=}')

    if request.method == 'POST':
        print(f'processing post request')
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            # print(vars(form.cleaned_data['topic']))
            my_id = form.cleaned_data['topic'].id
            return redirect('learning_logs:view_topic', my_id)
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = EntryForm(initial={'topic': topic_id})

    # Display blank or invalid form
    context = {
        "form": form,
    }
    return render(request, "learning_logs/create_entry.html", context)

def edit_entry(request, entry_id):

    print(f'in edit_entry()')
    print(f'{request.method=}')

    entry = Entry.objects.get(id=entry_id)

    if request.method == 'POST':
        print(f'processing post request')
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            my_id = form.cleaned_data['topic'].id
            return redirect('learning_logs:view_topic', my_id)
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = EntryForm(instance=entry)

    # Display blank or invalid form
    context = {
        "form": form,
        "entry": entry
    }
    return render(request, "learning_logs/edit_entry.html", context)
