from django.conf.urls import patterns, url
from django.views.generic import DetailView
from django.views.generic import DateDetailView
from django.views.generic import ArchiveIndexView
from django.views.generic import YearArchiveView
from django.views.generic import DayArchiveView
from django.views.generic import MonthArchiveView

from .models import News

urlpatterns = patterns('',
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<slug>.*)/$',
                DateDetailView.as_view(model=News, month_format='%m',
                date_field="date"), name="date_detail_news"
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
                MonthArchiveView.as_view(model=News, month_format='%m',
                date_field="date"), name="month_list_news"
    ),
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(model=News,
                date_field="date", make_object_list=True), name="year_list_news"
    ),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/$',
                DayArchiveView.as_view(model=News, month_format='%m',
                date_field="date"), name="date_list_news"
    ),
    url(r'^(?P<slug>.*)/$', DetailView.as_view(model=News),
                name='detail_news'
    ),
    url(r'^$', ArchiveIndexView.as_view(model=News, 
                date_field="date"), name='list_news'
    ),
)
