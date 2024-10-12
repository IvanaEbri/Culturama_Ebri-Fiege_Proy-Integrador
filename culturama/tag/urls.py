from django.urls import path
from .views import *

urlpatterns = [
    path('tags/see/<int:pk>/', TagSeeView.as_view(), name='SeeTag'),
    path('tags/add/', CreateTagView.as_view(), name='CreateTag'),
    path('tags/edit/<int:pk>/', TagEditView.as_view(), name='EditTag'),
]
