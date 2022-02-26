from django.db import models


class Pizza(models.Model):
    """ Класс пицца """
    name = models.CharField(max_length=100)

    def __str__(self):
        """Возвращает строковое представление модели """
        return self.name


class Topping(models.Model):
    """ Класс топпинги """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    class Meta:  # класс Meta вкладывается в класс Entry
        """ Класс Meta хранит дополнительную информацию по управлению моделью;
        в данном случае он позволяет задать специальный атрибут,
        который приказывает Django использовать форму множественного числа Entries при обращении
        более чем к одной записи. (Без этого Django будет использовать неправильную форму Entrys.)
        """
        verbose_name_plural = 'Toppings'

    def __str__(self):
        """ Возвращает строковое представление модели.
        Метод __str__() сообщает Django, какая информация должна отображаться при обращении к отдельным записям.
        Так как запись может быть достаточно длинным блоком текста, мы приказываем Django выводить
        только первые 50 символов. Также добавляется многоточие — признак вывода неполного текста.
        """
        return self.name
