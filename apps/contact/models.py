# -*- coding: utf-8 -*-
from django.db import models


class Contact(models.Model):
    name = models.CharField(u"nome", max_length=255)
    email = models.EmailField()
    subject = models.CharField(u"assunto", max_length=255)
    description = models.TextField(u"descrição")

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
