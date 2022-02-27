from django.shortcuts import render

from .models import Pizza


def index(request):
    """ Домашняя страница приложения pizzeria """
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """ Выводит список видов пиццы """
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    """ Выводит одну пиццу и все ее топпинги """
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
