# Django-model-util
from model_utils.models import TimeStampedModel 
# Django
from django.db import models


# Modelo de pagina principal
class Home (TimeStampedModel):
    
    title = models.CharField(
        'Nombre',
        max_length=50
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros', 
        max_length=50
    )
    contac_email = models.EmailField(
        'Email de Contacto', 
        blank=True,
        null=True,
    )
    phone = models.CharField(
        'Telefono Contacto', 
        max_length=20,
        blank=True,
        null=True,
    )
    
    class Meta:
        
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
        
    def __str__(self):
        
        return self.title
    
    
# Suscribers
class Suscribers(TimeStampedModel):
    
    email = models.CharField( max_length=255)
    
    class Meta:
    
        verbose_name = 'Suscripto'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
        
        return self.email
    

# Contactos
class Contact(TimeStampedModel):
    
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.CharField( max_length=20)
    messagge = models.TextField()
    
    class Meta:

        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        
        return self.full_name
    