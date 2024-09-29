from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserConfirmLogoutView, AdminSiteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='Register'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('logout/', UserLogoutView.as_view(), name='Logout'),
    path('confirm_logout/', UserConfirmLogoutView.as_view(), name='ConfirmLogout'),
    path('admin-site/', AdminSiteView.as_view(), name='SitesAdmin'),
]
