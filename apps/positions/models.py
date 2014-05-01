#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:55:22
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(
                                  max_length=50,
                                  blank=True,
                                  null=True,
                                  help_text=''
                                )

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')
        app_label = 'positions'
