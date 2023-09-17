from django.db import models 


class EntryManager(models.Manager):
    
    # Entradas que van a ir a portada 
    def entrada_portada(self):
        
        return self.filter(
            puclic = True,
            portada = True,            
        ).order_by('-created').first()
        
    # Entradas que van a ir a los articulos 
    def entrada_articulos(self):
        
        return self.filter(
            puclic = True,
            in_home = True,            
        ).order_by('-created')[:4]
        
    # Entrada para articulos recientes
    def entrada_recientes(self):
        
        return self.filter(
            puclic = True,         
        ).order_by('-created')[:6]
    
    # Busqueda por entrada o categoria
    def buscar_entrada(self, kword, categoria):
        
        if len(categoria) > 0:
            
            return self.filter(
            category__short_name = categoria,
            title__icontains = kword,
            puclic = True
            ).order_by('-created')

        else:
            
            return self.filter(
                title__icontains = kword,
                puclic = True
            ).order_by('-created')