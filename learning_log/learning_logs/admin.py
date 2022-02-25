from django.contrib import admin

# Точка сообщает Django, что файл models.py следует искать в одном каталоге с admin.py
from .models import Topic, Entry

# сообщает Django, что управление моделью должно осуществляться через административный сайт
admin.site.register(Topic)
admin.site.register(Entry)
