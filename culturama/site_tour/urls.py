from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', SitesAdminView.as_view(), name='SitesAdmin'),
    path('create/', CreateSiteView.as_view(), name='CreateSite'),
    path('edit/<int:pk>/', EditarSiteView.as_view(), name='EditSite'),
    path('delete/<int:pk>/', EliminarSiteView.as_view(), name='DeleteSite'),
]
