from django.contrib import admin

from .models import Borrowed_Book
from BookManagment.models import Book


admin.site.register(Borrowed_Book)
