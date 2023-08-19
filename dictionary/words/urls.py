from django.urls import path

from .views import CreateEntryView, EntriesList

app_name = 'words'

urlpatterns = [
    path('', CreateEntryView.as_view(), name='home'),
    path('words', EntriesList.as_view(), name='words'),
]
