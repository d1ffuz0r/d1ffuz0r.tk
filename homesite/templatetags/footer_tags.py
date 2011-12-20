from django import template
from homesite.forms import QuickContactForm
from homesite.models import Blog, Settings
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.simple_tag
def quick_form():
    """
       Quick message form
       Example: {% quick_form %}
    """
    return QuickContactForm().as_p()


@register.simple_tag(takes_context=True)
def social(context):
    """
    Settings for getting social links
    """
    try:
        settings = Settings.objects.get()
    except ObjectDoesNotExist:
        settings = None
    context["social"] = settings
    return u""


@register.simple_tag(takes_context=True)
def latest_posts(context):
    """
       Latest posts in blog
       example: {{ latest_posts }}
                {% for post in latest_posts %}
                 ...
                {% endfor %}
    """
    try:
        posts = Blog.objects.all()[:4]
    except ObjectDoesNotExist:
        posts = None
    context["latest_posts"] = posts
    return u""
