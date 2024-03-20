from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  
    list_filter = ('role',)  

admin.site.register(CustomUser, CustomUserAdmin)
