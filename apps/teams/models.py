#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:11
from django.utils.translation import ugettext_lazy as _
from django.db import models


def upload():
    pass


class Team(models.Model):
    """
    """    
    name = models.CharField(_('Team name'), max_length=200)
    city = models.ForeignKey('addresses.City')
    emblem = models.ImageField(upload_to=upload)
    created_on = models.DateTimeField(auto_now=True)
    about = models.TextField(
        blank=True,
        null=True,
        help_text=_('Some informations about the Team')
        )

    def __unicode__(self):
        return u'%s' % self.name
