from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from job.sitemaps import StaticViewSitemap, BlogSitemap, HomeStatic, ProjectSitemap
import job.views
import body.views

handler404 = job.views.error_404
handler500 = job.views.error_500

sitemaps = {
    'home': HomeStatic,
    'static': StaticViewSitemap,
    'blogs': BlogSitemap,
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('ioqw8k9qw/', admin.site.urls),
    path('', job.views.home, name = 'home'),
    path('blogs/', include('body.urls'), name = 'blogs'),
    path('projects/', body.views.projects, name='project'),
    path('projects/<int:project_id>/', body.views.projdetails, name='projdetails'),
    path('privacy/', job.views.privacy, name='privacy'),
    path('terms/', job.views.terms, name='term'),
    path('contact/', job.views.contacts, name='contact'),
    path('fdbk/msg/', job.views.contactlst, name='contactlist'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps})
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
