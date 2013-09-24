# -*- coding: utf-8 -*-
from django.db import models


class Question(models.Model):
    question = models.CharField(u"pergunta", max_length=255)
    active = models.BooleanField(u"ativo", default=True)
    date = models.DateField(u"data", auto_now_add=True)

    def __unicode__(self):
        return u"{}".format(self.question)

    class Meta:
        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'


class Alternative(models.Model):
    question = models.ForeignKey(Question, related_name=u"pergunta")
    alternative = models.CharField(u"alternativa", max_length=255)
    vote = models.IntegerField(u"votos", blank=True, null=True, default=0)

    def __unicode__(self):
        return u"{}".format(self.alternative)
