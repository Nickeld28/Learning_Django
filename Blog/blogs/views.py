from django.shortcuts import render, redirect

from .forms import PostForm
from .models import BlogPost


def index(request):
    """ Домашняя страница приложения blogs """
    posts = BlogPost.objects.order_by('date_added')
    return render(request, 'blogs/index.html', {'posts': posts})


def new_post(request):
    """Добавляет новый пост """
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PostForm()

    else:
        # Отправлены данные POST; обработать данные.
        form = PostForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('blogs:index')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    """ Редактирует существующий пост """
    post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
    # Исходный запрос; форма заполняется данными текущей записи.
        form = PostForm(instance=post)
    else:
        # Отправка данных POST; обработать данные.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def post(request, post_id):
    """ Выводит один пост """
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)
