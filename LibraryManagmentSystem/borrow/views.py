from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Borrowed_Book
from BookManagment.models import Book

@login_required
def borrow_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        user = request.user
        borrowed_books_count = Borrowed_Book.objects.filter(user=user).count()
        if borrowed_books_count < 3:
            if book.status == Book.Status.AVAILABLE:
                Borrowed_Book.objects.create(user=user, book=book)
                book.status = Book.Status.BORROWED
                book.save()
                return redirect('book_list')
            else:
                return render(request, 'error.html', {'message': 'This book is not available for borrowing.'})
        else:
            return render(request, 'error.html', {'message': 'You have already borrowed 3 books.'})


    book = Book.objects.get(id=book_id)
    borrowed_books = Borrowed_Book.objects.filter(book=book).select_related('user')
    return render(request, 'borrow_book.html', {'book': book, 'borrowed_books': borrowed_books})
