from django.forms import models
from django import forms

from .models import Entry


class EntryForm(models.ModelForm):
    class Meta:
        model = Entry
        fields = ['word', 'translation', 'context']

        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control left-input mr-4',
                                           'placeholder': 'New Word'}),
            'translation': forms.TextInput(attrs={'class': 'form-control left-input ml-4',
                                           'placeholder': 'Translation'}),
            'context': forms.TextInput(attrs={'class': 'form-control mb-4 center-input',
                                              'placeholder': 'Context'}),

        }
