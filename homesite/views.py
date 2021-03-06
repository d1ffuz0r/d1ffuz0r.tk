# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404
from models import Blog
from homesite.forms import QuickContactForm
from django.http import HttpResponse
from decorators import render_to


@render_to("blog.haml")
def blog_list(request):
    posts_list = Blog.objects.all()
    paginator = Paginator(posts_list, 5)
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return {"page": "blog", "posts": posts}


@render_to("post.haml")
def blog_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return {"page": "blog", "post": post}


def quick_form(request):
    if request.is_ajax():
        form = QuickContactForm(request.POST)
        if form.is_valid():
            message = u"Success. your message sended"
            form.save()
        else:
            message = u"Error. Please check data"
    else:
        message = u"Not data"
    return HttpResponse(message)


@render_to('404.haml')
def error404(request):
    return {}


@render_to('500.haml')
def error500(request):
    return {}
