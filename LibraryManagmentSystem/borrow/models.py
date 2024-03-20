from django.db import models
from BookManagment.models import Book
from django.contrib.auth.models import User # link it to user app and use CustomUser, if it could be


class Borrowed_Book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} (by {self.book.author} )"
