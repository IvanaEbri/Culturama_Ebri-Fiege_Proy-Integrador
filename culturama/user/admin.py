from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'password', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(User, UserAdmin)