from django import template
from homesite.forms import QuickContactForm
from homesite.models import Blog

register = template.Library()

@register.simple_tag
def quick_form():
    '''
    quick message form
    use: {% quick_form %}
    '''
    return QuickContactForm().as_p()

@register.simple_tag(takes_context=True)
def latest_posts(context):
    '''
    latest posts in blog
    use: {{ latest_posts }}
    example: {% for post in latest_posts %}
                 ...
             {% endfor %}
    '''
    posts = Blog.objects.order_by('-id')[:4]
    context['latest_posts'] = posts
    return u''