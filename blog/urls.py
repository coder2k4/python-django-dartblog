from django.urls import path

from . views import *


app_name = "blog"

urlpatterns = [
    path('<str:slug>/', Category.as_view(), name='category'),
    path('<str:slug_category>/<str:slug>/', Post.as_view(), name='post'),
    path('tag/<str:slug>', PostByTag.as_view(), name='tag'),
    path('posts/all/search/', SearchPost.as_view(), name='search'),
]
