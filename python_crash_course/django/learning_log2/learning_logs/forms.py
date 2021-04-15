from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'text label'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['topic', 'text', ]
        labels = {'topic': 'select topic',
                  'text': 'your entry',
                  }
        widgets = {'text': forms.Textarea(
            attrs={'cols': 80,
                   'placeholder': 'Enter entry information here',
                   'autofocus': 'autofocus'})}
