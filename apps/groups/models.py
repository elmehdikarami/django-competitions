#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:38:40
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey('seasons.Season', related_name='groups')
    teams = models.ManyToManyField('teams.Team', related_name='groups')

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        app_label = 'groups'

    def __unicode__(self):
        return u'%s' % self.name
