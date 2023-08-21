from django.shortcuts import render,  redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Entry
from .forms import EntryForm, UserAuthenticationForm

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'words/input_entry.html'
    success_url = reverse_lazy('words:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEntryView, self).form_valid(form)

class EntriesListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'words/entries_list.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.filter(user_id=self.request.user.pk).order_by('-time_updated')


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EntryForm
    model = Entry
    template_name = 'words/input_entry.html'
    success_url = reverse_lazy('words:words')
    context_object_name = 'entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_entry'] = True
        return context

class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('words:words')
    template_name = 'words/delete_entry.html'

class UserLogin(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'words/login_user.html'
    next_page = reverse_lazy('words:home')


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'words/register.html'
    next_page = reverse_lazy('words:home')


def logout_user(request):
    logout(request)
    return redirect('words:home')

