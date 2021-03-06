""" Определяет схемы URL для learning_logs """  # строка документации показывает с какой версией urls.py работаем

# импортируется функция path для связывания URL с представлениями (views)
from django.urls import path

# точка указывает на то, что Python должен импортировать views из каталога, в котором находится текущий модуль urls.py
from . import views

# переменная app_name помогает django отличить этот файл urls.py от одноименных файлов в других приложениях
app_name = 'learning_logs'

# переменная urlpatterns - это список страниц, которые могут запрашиваться из приложения learning_logs
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),

    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
