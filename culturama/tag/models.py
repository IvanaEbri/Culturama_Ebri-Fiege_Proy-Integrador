from django.db import models

class Tag(models.Model):
    id_tag = models.AutoField(primary_key=True)  #autofield
    tag = models.CharField(max_length=20, unique=True, verbose_name='Etiqueta')

    def __str__(self):
        return self.tag

class Site_tag(models.Model):
    id_site_tag = models.AutoField(primary_key=True)  # autofield
    id_site = models.ForeignKey('site_tour.Site_tour', on_delete=models.CASCADE, null=False, blank=False)
    id_tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.id_tag.tag
