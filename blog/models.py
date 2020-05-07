from django.db import models

# Create your models here.
from django.urls import reverse

from core.models import TimeStampedModel


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок категории')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='Url')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category', args=[str(self.id)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя тэга')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='Url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(TimeStampedModel):
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url')
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Пост')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фотография')
    view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='Тэги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-updated']
