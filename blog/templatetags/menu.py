from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('tags/menu.html', takes_context=True)
def show_menu(context, menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class, "context": context}
