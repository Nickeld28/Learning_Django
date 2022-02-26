from django.shortcuts import render


def index(request):
    """ Домашняя страница приложения meal_plans """
    return render(request, 'meal_plans/index.html')
