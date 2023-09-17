#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'list-entry/',
        views.EntryListView.as_view(),
        name='list-entry'
    ),
    path(
        'entry/<pk>/',
        views.EntryDetailView.as_view(),
        name='detail-entry'
    ),
]