from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='Registro'),
    path('login/', UserLoginView.as_view(), name='Login'),
]
