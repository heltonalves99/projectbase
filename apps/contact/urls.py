from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import ContactCreateView

urlpatterns = patterns('',
    url(r'^$', ContactCreateView.as_view(), name='contact_add'),
    url(r'^success/', TemplateView.as_view(template_name="contact/success.html")),
)
