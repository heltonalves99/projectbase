# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Question


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question

