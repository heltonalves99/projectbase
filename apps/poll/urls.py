from django.conf.urls import patterns, url

from .views import QuestionListView
from .views import QuestionDetailView
from .views import QuestionRedirectView

urlpatterns = patterns('',
    url(r'^$', QuestionListView.as_view(), name='question_list'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^(?P<pk>\d+)/vote/$', QuestionRedirectView.as_view(), name='question_vote'),
)
