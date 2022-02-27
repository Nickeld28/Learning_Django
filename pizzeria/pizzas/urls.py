""" Определяет схемы URL для pizzas """


from django.urls import path

from . import views


app_name = 'pizzas'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),

    # Страница со списком всех видов пиццы
    path('pizzas/', views.pizzas, name='pizzas'),

    # Страница с подробной информацией по отдельной пицце
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]
