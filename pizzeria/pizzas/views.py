from django.shortcuts import render


def index(request):
    """ Домашняя страница приложения pizzeria """
    return render(request, 'pizzas/index.html')