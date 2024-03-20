from django.urls import path
from . import views
from django.http import HttpResponse
def home_borrow(request):
    return HttpResponse('Borrow page "\n" Welcome to Borrow system !')

urlpatterns = [
    path('',home_borrow),
    #path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
]