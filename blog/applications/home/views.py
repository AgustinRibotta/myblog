# Python
import datetime
# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView
)
# Applications.entrada
from applications.entrada.models import Entry
# Models 
from .models import Home


class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamois el home
        context['home'] = Home.objects.latest('created')
        # Portada
        context['protada'] =  Entry.objects.entrada_portada()
        # Arcticulos portada
        context['arcticulos'] =  Entry.objects.entrada_articulos()
        # Entradas  recientes
        context['recientes'] =  Entry.objects.entrada_recientes()
        return context
    



