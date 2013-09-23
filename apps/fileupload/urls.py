from django.conf.urls import patterns
from .views import image_create

urlpatterns = patterns(
    '',
    (r'^image/(?P<gallery_pk>\d+)/$', image_create, {}, 'upload-new'),
    # (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
)
