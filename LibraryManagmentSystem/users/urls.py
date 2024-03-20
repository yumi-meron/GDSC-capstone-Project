from django.urls import path
from . import views
from django.http import HttpResponse 
def user_home(request):
    return render(request, 'users/base.html')

urlpatterns = [
    path('',user_home),
    path('register/',views.register),
    path('profile/',views.profile),
]# login mnamn have tobe added