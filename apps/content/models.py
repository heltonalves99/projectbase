# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class Content(models.Model):
    father = models.ForeignKey('Content',
            related_name=u"pai", help_text=u"caso a página tenha um pai.",
            blank=True, null=True)
    title = models.CharField(u"título da página", max_length=255, unique=True)
    content = RichTextField(config_name='project_ckeditor')
    active = models.BooleanField(u"página ativa", default=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdos"

    def __unicode__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return u"{}".format(self.slug)
