from django.urls import path

from .views import *

app_name = 'words'

urlpatterns = [
    path('', CreateEntryView.as_view(), name='home'),
    path('words', EntriesList.as_view(), name='words'),
    path('words/<int:pk>', EntryUpdateView.as_view(), name='update')
]
