from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 
from .forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'password', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(User, UserAdmin)