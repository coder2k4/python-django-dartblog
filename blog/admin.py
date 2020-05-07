from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# CKEDITOR WIDGET
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Post
        fields = '__all__'


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ['tags']
    list_display_links = ['title', 'slug']
    list_filter = ['tags', 'category']
    search_fields = ['title',
                     'author',
                     'content',
                     'photo',
                     'view', ]
    form = PostAdminForm

    list_display = [
        'title',
        'slug',
        'author',
        'content',
        'view',
        'category',
        'created',
        'updated',
        'get_photo'
    ]

    fieldsets = (
        (None, {
            'fields': ('title',
                       'slug',
                       'author',
                       'content',
                       'category',
                       'tags',
                       'view',
                       'created',
                       'updated',
                       )
        }),
        ('Загрузить фотографию', {
            'classes': ('wide',),
            'fields': ('get_photo','photo')
        }),
    )

    readonly_fields = ['view', 'created', 'updated', 'get_photo']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src={obj.photo.url} width=50/>")
        return "-"

    get_photo.short_description = "Превью"
