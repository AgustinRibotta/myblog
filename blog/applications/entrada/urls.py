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
        'entry/<slug>/',
        views.EntryDetailView.as_view(),
        name='detail-entry'
    ),
]