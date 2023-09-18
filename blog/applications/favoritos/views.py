# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import  (
    View,
    ListView,
    DeleteView,
    )
# Models
from .models import Favorites
# Apllication Entradas
from applications.entrada.models import Entry



class UserListView(LoginRequiredMixin, ListView):
    
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy ('users_app:user-login')
    
    def get_queryset(self):
        
        return Favorites.objects.entradas_user(self.request.user)


class AddFavoriteView(LoginRequiredMixin, View):
    
    login_url = reverse_lazy ('users_app:user-login')
    context_object_name = 'favorito'
    
    def post(self, request, *args, **kwargs):
        # Recuperamos el usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        
        # Verifica si ya existe un registro en favoritos para el mismo usuario y entrada
        favorito_existente = Favorites.objects.filter(user=usuario, entry=entrada).first()
        
        if favorito_existente is None:
        # Registro favorito
            Favorites.objects.create(
                user = usuario,
                entry = entrada,
            )
        
        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
            
        )
        


class FavoritesDeleteView(LoginRequiredMixin, DeleteView):
    
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
 
