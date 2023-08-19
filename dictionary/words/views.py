from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Entry
from .forms import EntryForm

class CreateEntryView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'words/index.html'
    success_url = reverse_lazy('words:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEntryView, self).form_valid(form)


