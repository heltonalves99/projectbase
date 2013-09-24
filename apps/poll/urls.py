from django.conf.urls import patterns, url

from .views import QuestionListView
from .views import QuestionDetailView

urlpatterns = patterns('',
    url(r'^$', QuestionListView.as_view(), name='question_list'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question_detail'),
)
