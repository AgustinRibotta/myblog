#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageViewTemplateView.as_view(),
        name='index',
    ),  
    path(
        'register-suscription', 
        views.SuscriberCreateView.as_view(),
        name='suscription',
    ), 
    path(
        'register-contact', 
        views.ContacCreateView.as_view(),
        name='contact',
    ),   
]