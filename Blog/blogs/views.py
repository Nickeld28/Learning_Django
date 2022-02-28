from django.shortcuts import render

from .models import BlogPost

def index(request):
    """ Домашняя страница приложения blogs """
    posts = BlogPost.objects.order_by('date_added')
    return render(request, 'blogs/index.html', {'posts': posts})
