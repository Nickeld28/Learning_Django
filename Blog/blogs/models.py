from django.db import models


class Blog(models.Model):
    """ Блог, который ведет пользователь """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Возвращает строковое представление модели """
        return self.text


class BlogPost(models.Model):
    """ Информация, опубликованная пользователем  """
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Класс Meta хранит дополнительную информацию по управлению моделью;
        в данном случае он позволяет задать специальный атрибут,
        который приказывает Django использовать форму множественного числа BlogPosts при обращении
        более чем к одной записи.
        """
        verbose_name_plural = 'blog posts'

    def __str__(self):
        """ Возвращает строковое представление модели.
        Метод __str__() сообщает Django, какая информация должна отображаться при обращении к отдельным записям.
        Так как запись может быть достаточно длинным блоком текста, мы приказываем Django выводить
        только первые 50 символов. Также добавляется многоточие — признак вывода неполного текста.
        """
        if len(str(self.text)) > 50:
            return f"{self.text[:50]}..."
        return self.text
