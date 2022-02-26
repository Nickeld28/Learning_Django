""" Определяет схемы URL для pizzas """


from django.urls import path

from . import views


app_name = 'pizzas'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]
