# Djeango
from django.db import models
from django.conf import settings
# Applications.Entradas
from applications.entrada.models import Entry
# Django-model-util
from model_utils.models import TimeStampedModel 
# Managers
from .managers import FavoriteManager


# Favoritos 
class Favorites (TimeStampedModel):
    
    user = models.ForeignKey(
        # Nos pemite llamar al user que estamos creando
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    entry = models.ForeignKey(
        Entry,
        related_name='Entry_favorites',
        on_delete=models.CASCADE
    )
    
    objects = FavoriteManager()
    
    class Meta:
        unique_together = ('user', 'entry')            
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'
        
    def __str__ (self):
        return self.entry.title
        
           