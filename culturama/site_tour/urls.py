from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', SitesAdminView.as_view(), name='SitesAdmin'),
    path('create/', CreateSiteView.as_view(), name='CreateSite'),
    path('edit/<int:pk>/', EditSiteView.as_view(), name='EditSite'),
    path('delete/<int:pk>/', DeleteSiteView.as_view(), name='DeleteSite'),
    path('see/<int:pk>/', SeeSiteAdminView.as_view(), name='SiteSeeAdmin'),
]
