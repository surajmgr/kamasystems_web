from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from body.models import blog, project
import body.urls

class HomeStatic(Sitemap):
    priority = 1
    changefreq = 'daily'
    protocol = "https"

    def items(self):
        return['home']

    def location(self, item):
        return reverse(item)

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'
    protocol = "https"

    def items(self):
        return[
            'blogs',
            'project',
            'privacy',
            'contact',
            'term',
            'contactlist'
        ]

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    priority = 0.64
    changefreq = 'daily'
    protocol = "https"

    def items(self):
        return project.objects.all()

    def location(self, item):
        url = '/projects/' + str(item.id)
        return url

class BlogSitemap(Sitemap):
    priority = 0.6
    changefreq = 'daily'
    protocol = "https"

    def items(self):
        return blog.objects.all()

    def location(self, item):
        url = '/blogs/' + str(item.id)
        return url