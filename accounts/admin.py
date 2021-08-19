from django.contrib import admin
from .forms import UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = [field.name for field in CustomUser._meta.fields]
    ordering = ['id']
    search_fields = ['id', 'email']
