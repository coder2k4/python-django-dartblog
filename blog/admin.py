from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
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
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ['tags']
    form = PostAdminForm
