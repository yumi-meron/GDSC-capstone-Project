from django.urls import path
from . import views

urlpatterns = [
    path('booklist/', views.book_list, name='book_list'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('addbook/', views.add_book, name='add_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]