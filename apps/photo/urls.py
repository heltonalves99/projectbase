from django.conf.urls import patterns, url

from .views import GalleryListView
from .views import GalleryDateDetailView

urlpatterns = patterns('',
    url(r'^$', GalleryListView.as_view(), name='gallery_list'),
    url(r'^(?P<year>\d+)/(?P<month>\d{1,2})/(?P<day>\d+)/(?P<slug>.*)/$',
                GalleryDateDetailView.as_view(), name="gallery_detail"),
)
