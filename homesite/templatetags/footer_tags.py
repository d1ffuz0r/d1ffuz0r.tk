from django import template
from homesite.forms import QuickContactForm
from homesite.models import Blog, Settings

register = template.Library()


@register.simple_tag
def quick_form():
    """quick message form
       Example: {% quick_form %}
    """
    return QuickContactForm().as_p()


@register.simple_tag(takes_context=True)
def social(context):
    settings = Settings.objects.all()[0]
    context["social"] = settings
    return u""


@register.simple_tag(takes_context=True)
def latest_posts(context):
    """latest posts in blog
       example: {{ latest_posts }}
                {% for post in latest_posts %}
                 ...
                {% endfor %}
    """
    posts = Blog.objects.all()[:4]
    context["latest_posts"] = posts
    return u""
