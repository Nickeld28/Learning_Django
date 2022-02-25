from django.contrib import admin

from .models import Topic  # Точка сообщает Django, что файл models.py следует искать в одном каталоге с admin.py

admin.site.register(Topic)  # сообщает Django, что управление моделью должно осуществляться через административный сайт
