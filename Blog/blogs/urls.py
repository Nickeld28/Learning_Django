""" Определяет схемы URL для blogs """

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),

    # Страница для редактирования записи
    path('new_post/', views.new_post, name='new_post'),

    # Страница с подробной информацией о посте
    path('post/<int:post_id>/', views.post, name='post'),

    # Страница для редактирования записи
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
