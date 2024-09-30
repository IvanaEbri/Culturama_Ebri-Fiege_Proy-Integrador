from django.db import models

# Create your models here.
class Tag (models.Model):
    id_tag = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=20, unique=True, blank=True, verbose_name='Etiqueta')

    def __str__(self):
        return self.tag

class Site_tag(models.Model):
    id_site_tag = models.IntegerField(primary_key=True)
    site_tour = models.ForeignKey('site_tour.Site_tour', on_delete=models.CASCADE, null=False, blank=False)
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return (f"{self.site_tour} - {self.tag}")

    class Meta:
        unique_together = ('site_tour', 'tag')