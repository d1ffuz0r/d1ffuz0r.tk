from django.contrib.syndication.views import Feed
from models import Blog


class BlogRss(Feed):
    title_template = "d1ffuz0r blog feed"
    link = "/blog/"
    description_template = "Posts on d1ffuz0r.tk blog"

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
