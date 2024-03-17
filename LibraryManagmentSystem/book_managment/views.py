from django.shortcuts import render, redirect, get_object_or_404
from .forms import  BookForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.user.is_authenticated and (request.user.role == 'admin' or request.user.role == 'superadmin'):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm()
        return render(request, 'add_book.html', {'form': form})
    else:
        return redirect('book_list')

def edit_book(request, book_id):
    if request.user.is_authenticated and (request.user.role == 'admin' or request.user.role == 'superadmin'):
        book = get_object_or_404(Book, id=book_id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm(instance=book)
        return render(request, 'edit_book.html', {'form': form})
    else:
        return redirect('book_list')

def delete_book(request, book_id):
    if request.user.is_authenticated and (request.user.role == 'admin' or request.user.role == 'superadmin'):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('book_list')
    else:
        return redirect('book_list')

