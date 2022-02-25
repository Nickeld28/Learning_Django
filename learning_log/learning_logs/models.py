from django.db import models

"""
Мы создали класс с именем Topic, наследующий от Model — родительского класса, включенного в Django
и определяющего базовую функциональность модели. В класс Topic добавляются два атрибута: text и date_added.
"""


class Topic(models.Model):
    """ Тема, которую изучает пользователь """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Возвращает строковое представление модели """
        return self.text
