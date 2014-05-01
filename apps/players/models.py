#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 01:10:40
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(blank=True, null=True, max_length=100)
    position = models.ForeignKey('positions.Position', blank=True, null=True)
    team = models.ForeignKey('teams.Team', related_name='players')
    is_captain = models.BooleanField(default=False)
    city = models.ForeignKey('addresses.City', related_name='players')
    about = models.TextField(
                            blank=True,
                            null=True,
                            help_text=_('Some informations about the Player')
                            )

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')
        app_label = 'players'
