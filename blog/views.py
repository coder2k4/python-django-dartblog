from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models


def index(request):
    return render(request, 'blog/index.html')


def category(request, slug):
    return render(request, 'blog/index.html')


class Home(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8
    paginate_orphans = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница мега блока'
        return context


class Category(ListView):
    paginate_by = 8
    paginate_orphans = 5
    context_object_name = 'posts'

    def get_queryset(self):
        return models.Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = models.Category.objects.get(
            slug=self.kwargs['slug'])
        return context


class Post(DetailView):

    model = models.Post

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object.view = F('view') + 1
        self.object.save()
        # Обязательно нужно перезагрузить поле из БД иначе будет текстовое представление строки F
        self.object.refresh_from_db()
        return super().get_context_data(**kwargs)


class PostByTag(ListView):
    paginate_by = 8
    paginate_orphans = 8
    context_object_name = 'posts'

    def get_queryset(self):
        print(self.kwargs['slug'])
        return models.Post.objects.filter(tags__slug=str(self.kwargs['slug']))
