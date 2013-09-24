from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from core.views import Home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$', Home.as_view()),
    url(r'^contact/', include('apps.contact.urls')),
    url(r'^gallery/', include('apps.photo.urls')),
    (r'^fileupload/', include('apps.fileupload.urls')),
    url(r'^poll/', include('apps.poll.urls')),
    url(r'', include('apps.content.urls')),
)

if settings.DEBUG:
    urlpatterns += (
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
    )
