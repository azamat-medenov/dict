from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Entry
from .forms import EntryForm

class CreateEntryView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'words/input_entry.html'
    success_url = reverse_lazy('words:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEntryView, self).form_valid(form)

class EntriesListView(ListView):
    model = Entry
    template_name = 'words/entries_list.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.order_by('-time_updated')


class EntryUpdateView(UpdateView):
    form_class = EntryForm
    model = Entry
    template_name = 'words/input_entry.html'
    success_url = reverse_lazy('words:words')
    context_object_name = 'entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_entry'] = True
        return context

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('words:words')
    template_name = 'words/delete_entry.html'

