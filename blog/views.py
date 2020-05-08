from django.shortcuts import render
from django.views.generic import ListView

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
