from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserConfirmLogoutView, AdminSiteView, TemplateView, Route1View, Route2View, AnswerView, map_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='Register'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('logout/', UserLogoutView.as_view(), name='Logout'),
    path('confirm_logout/', UserConfirmLogoutView.as_view(), name='ConfirmLogout'),
    path('admin-site/', AdminSiteView.as_view(), name='SitesAdmin'),
    path('home_user/', TemplateView.as_view(template_name='home_user.html'), name='HomeUser'),
    #rutas a acomodar
    path('map/', map_view, name='Map'),
    #path('map/', TemplateView.as_view(template_name='map.html'), name='Map'),
    path('route/', Route1View.as_view(), name='Route1'), 
    path('user/route2/<int:tag_id>/', Route2View.as_view(), name='Route2'),
    path('user/answer/<int:tag_id>/<str:cant_paradas>/', AnswerView.as_view(), name='Answer'),
]
