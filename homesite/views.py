from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404
from models import Services, Portfolio, Settings, About, Blog
from homesite.forms import QuickContactForm
from django.http import HttpResponse
from decorators import render_to

_ = lambda x: x

@render_to('home.html')
def home(request):
    settings = Settings.objects.get()
    return {'page': 'home', 'settings': settings}

@render_to('about.html')
def about(request):
    about = About.objects.get()
    return {'page': 'about', 'about': about}

@render_to('portfolio.html')
def portfolio(request):
    works = Portfolio.objects.all()
    return {'page': 'portfolio', 'works': works}

@render_to('services.html')
def services(request):
    services = Services.objects.all()
    return {'page': 'services', 'services': services}

@render_to('contacts.html')
def contacts(request):
    settings = Settings.objects.get()
    return {'page': 'contacts', 'settings': settings}

@render_to('blog.html')
def blog_list(request):
    posts_list = Blog.objects.order_by('-id').all()
    paginator = Paginator(posts_list,5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
        
    return {'page': 'blog', 'posts': posts}

@render_to('post.html')
def blog_post(request,post_id):
    post = get_object_or_404(Blog, id = post_id)
    return {'page': 'blog', 'post': post}

def quick_form(request):
    if request.is_ajax():
        form = QuickContactForm(request.POST)
        if form.is_valid():
            message = _('Success. your message sended')
            form.save()
        else:
            message = _('Error. Please check data')
    else:
        message = _('Not data')
    return HttpResponse(message)