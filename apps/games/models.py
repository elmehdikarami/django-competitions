#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 01:29:34
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Game(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    team_home = models.ForeignKey('teams.Team', related_name='home_games')
    team_away = models.ForeignKey('teams.Team', related_name='away_games')
    playoff = models.BooleanField('Is Playoff?', default=False)
    played = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    date = models.DateTimeField()
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    season = models.ForeignKey('seasons.Season', related_name='games')
    duration = models.IntegerField(_('Game duration in minutes'), default=90)
    detail = models.OneToOneField('GameDetail', related_name='game')

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
        app_label = 'games'

    def __unicode__(self):        
        return u'%s' % self.name
    

class GameDetail(models.Model):
    manually_points = models.BooleanField(default=False)
    city = models.ForeignKey('addresses.City', related_name='games_details')
    location  = models.CharField(max_length=100, blank=True, null=True)
    events = models.ManyToManyField('events.Event',
                                    related_name='games_details')

    class Meta:
        verbose_name = _('Game Detail')
        verbose_name_plural = _('Games Details')
        app_label = 'games'