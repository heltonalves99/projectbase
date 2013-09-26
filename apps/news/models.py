# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(u"título", max_length=255)
    short_title = models.CharField(u"título curto", max_length=255)
    short_description = models.CharField(u"descrição curta", max_length=255)
    content = RichTextField(config_name='project_ckeditor')
    image_home = models.ImageField(u"imagem em destaque", upload_to="image_news",
                                    blank=True, null=True)
    date = models.DateTimeField(u"data de publicação")
    active = models.BooleanField(u"ativo", default=True)
    slug = models.SlugField()

    def __unicode__(self):
        return u"{}".format(self.title)

    class Meta:
        verbose_name = u"Notícia"
        verbose_name_plural = u"Notícias"
        ordering = ('-date',)

    def get_absolute_url(self):
        args = [
            self.data.strftime("%Y"),
            self.data.strftime("%m"),
            self.data.strftime("%d"),
            self.slug
        ]
        return ('list_news', args)
