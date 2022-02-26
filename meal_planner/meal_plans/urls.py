""" Определяет схемы URL для meal_plans """


from django.urls import path

from . import views


app_name = 'meal_plans'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]
