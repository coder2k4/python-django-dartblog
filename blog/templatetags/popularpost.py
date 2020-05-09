from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('tags/popposts.html')
def popularpost(cnt=3):
    popposts = Post.objects.order_by('-view')[:cnt]
    return {"popposts": popposts}
