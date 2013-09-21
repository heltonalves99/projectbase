# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import DetailView

from .models import Content

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=Content,
        slug_field='slug'), name='page'),
)
