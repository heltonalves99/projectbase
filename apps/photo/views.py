# -*- coding: utf-8 -*-
from django.views.generic.dates import DateDetailView
from django.views.generic.list import ListView

from .models import Gallery


class GalleryListView(ListView):
    model = Gallery


class GalleryDateDetailView(DateDetailView):
    model = Gallery
    date_field = 'date'
    month_format = '%m'
