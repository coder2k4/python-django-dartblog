from django import template

from blog.models import Tag

register = template.Library()


@register.inclusion_tag('tags/tagscloud.html')
def tagscloud():
    tags = Tag.objects.all()
    return {'tagscloud': tags}
