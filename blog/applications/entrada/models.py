# Django
from django.db import models
from django.conf import settings
# Ckaeditor
from ckeditor_uploader.fields import RichTextUploadingField
# Django-model-util
from model_utils.models import TimeStampedModel 
# Mannager
from .managers import EntryManager


# Categorias
class Category (TimeStampedModel):
    
    short_name = models.CharField(
        'Nombre Corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )
    
    class Meta:
        
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        
        return self.name
    

# Etiquetas de articulos
class Tag (TimeStampedModel):

    name = models.CharField(
        'Nombre',
        max_length=30,
    )

    class Meta:
        
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        
        return self.name
    

# Modelo de entradas o articulos   
class Entry (TimeStampedModel):
    
    user = models.ForeignKey(
        # Nos pemite llamar al user que estamos creando
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE    
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=50
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField(
        'Contenido',
        default=True,
        null=True 
    )

    image = models.ImageField(
        'Imagen', 
        upload_to='Entry',
        blank=True
    )
    puclic = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(
        editable=False,
        max_length=300
    )
    
    objects = EntryManager()
    
    class Meta:
        
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
    def __str__(self):
        
        return self.resume
    
    
