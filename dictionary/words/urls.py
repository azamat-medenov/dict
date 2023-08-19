from django.urls import path

from .views import CreateEntryView

app_name = 'words'

urlpatterns = [
    path('', CreateEntryView.as_view(), name='home'),
]
