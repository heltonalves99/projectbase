# -*- coding: utf-8 -*-
from django.db import models


class Gallery(models.Model):
    title = models.CharField(u"título", max_length=255)
    description = models.TextField(u"descrição", blank=True, null=True)
    date = models.DateTimeField(u"data")
    active = models.BooleanField(u"ativo", default=True)
    slug = models.SlugField()

    def __unicode__(self):
        return u"{}".format(self.title)

    class Meta:
        verbose_name = u"Galeria de fotos"
        verbose_name_plural = u"Galeria de fotos"
        ordering = ["-date"]

    @models.permalink
    def get_absolute_url(self):
        args = [
            self.date.strftime("%Y"),
            self.date.strftime("%m"),
            self.date.strftime("%d"),
            self.slug
        ]
        return ('gallery_detail', args)


class Image(models.Model):
    gallery = models.ForeignKey("Gallery")
    image = models.ImageField(u"imagem", upload_to="photos", blank=True, null=True)
    legend = models.CharField(u"legenda", max_length=255)

    def __unicode__(self):
        if self.legend:
            return u"{0}-{1}".format(self.id, self.legend)
        return u"{}".format(self.id)

    class Meta:
        verbose_name = u"Imagem"
        verbose_name_plural = u"Imagens"
