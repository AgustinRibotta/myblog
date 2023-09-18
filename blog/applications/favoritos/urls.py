#
from django.urls import path

from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/',
        views.UserListView.as_view(),
        name='perfil'
    ),
    path(
        'add-favorito/<pk>/',
        views.AddFavoriteView.as_view(),
        name='favorito'
    ),
    path(
        'delete-favorito/<pk>/',
        views.FavoritesDeleteView.as_view(),
        name='delete'
    ),
]