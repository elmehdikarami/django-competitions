#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 01:26:52
from django.utils.translation import ugettext_lazy as _
from django.db import models


def upload_image_coutry():
    pass


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to=upload_image_coutry)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        app_label = 'addresses'

    def __unicode__(self):
        return u'%s' % self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    country = models.ForeignKey(Country, related_name='cities')

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        app_label = 'addresses'

    def __unicode__(self):
        return u'%s' % self.name
