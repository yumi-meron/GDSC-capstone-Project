from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    
    list_display = ['id','title', 'author', 'genre', 'status']
    list_filter =  ['status', 'genre', 'author']
    search_fields =['title', 'id']

admin.site.register(Book,BookAdmin)
admin.site.site_header=('Welcome to our Library!!!')