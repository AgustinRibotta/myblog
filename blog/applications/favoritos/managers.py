from django.db import models


class FavoriteManager (models.Manager):
    
    def entradas_user (self, usuario):
        
        return self.filter(
            entry__puclic = True,
            user=usuario
        ).order_by('-created')