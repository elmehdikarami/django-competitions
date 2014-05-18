#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-18 11:21:45
from django.utils.translation import ugettext_lazy as _
from django.db import models


def upload_to_events():
    pass

class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('0', _('Player event')),
        ('1', _('Team event')),
    )
    name = models.CharField(
        max_length=100,
        help_text=_("i.e. Yellow Card, Goal, Red Card, " \
                    "Own Goal(goal against his/her team)...")
                    )
    player_event = models.BooleanField(
        default=True,
        help_text=_("Specify whether or not it's a player event, if not " \
                    "then it can be applied to teams")
                    )
    picture = models.ImageField(upload_to=upload_to_events)
    player = models.ForeignKey('players.Player', related_name='events')
    team = models.ForeignKey('teams.Team', related_name='events')

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        app_label = 'events'
