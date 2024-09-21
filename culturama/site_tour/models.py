import os
from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

# Create your models here.
TYPE = [(1,'Interior'),(2,'Exterior')]

class Site_tour(models.Model):
    id_site_tour = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=100, verbose_name='Nombre', blank=True)
    description = models.TextField(verbose_name='Descripcion', blank=True)
    url = models.URLField(verbose_name='Url')
    image = models.ImageField( null=True, blank=True, verbose_name='Imagen')
    adress = models.CharField(max_length=100, verbose_name='Dirección', null=True, blank=True)
    coordinates = models.CharField(max_length=100, null=True, blank=True, verbose_name='Coordenadas')
    journey_time = models.TimeField(null=True, blank=True, verbose_name='Tiempo de recorrido')
    site_type = models.IntegerField(choices=TYPE, default=TYPE[0][0], verbose_name='Tipo', null=True, blank=True)
    accesibility = models.TextField(null=True, blank=True, verbose_name='Accesibilidad')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.site_name

    def get_type_display(self):
        return dict(TYPE).get(self.site_type, "Desconocido")

    def save(self, *args, **kwargs):
        # Si hay una imagen, definir el formato y la ubicación de guardado
        if self.image:
            img = Image.open(self.image)

            # Convertir siempre a JPEG
            if img.format != 'JPEG':
                img = img.convert('RGB')

            file_name, _ = os.path.splitext(self.image.name)
            file_name = f"{file_name}.jpg"  # Siempre guardaremos en formato JPEG

            # Guardar la imagen en la ubicación definida con el formato especificado
            img_io = BytesIO()
            img.save(img_io, format='JPEG')
            img_content = ContentFile(img_io.getvalue(), file_name)

        # Guardar el resto de los campos del modelo
        super().save(*args, **kwargs)