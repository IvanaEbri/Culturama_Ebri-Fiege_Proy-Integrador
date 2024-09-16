from django.urls import path
from site_tour.views import SitesAdminView

urlpatterns = [
    path('admin/', SitesAdminView.as_view(), name='SitesAdmin'),
]
