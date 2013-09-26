# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Question
from .models import Alternative


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


class QuestionRedirectView(RedirectView):
    def post(self, request, *args, **kwargs):
        alternative = Alternative.objects.get(id=request.POST['alternative'])
        alternative.vote += 1
        alternative.save()
        messages.success(request, u"Seu voto foi enviado com sucesso.")
        return super(QuestionRedirectView, self).post(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse_lazy('poll:question_detail', args=[kwargs['pk']])

