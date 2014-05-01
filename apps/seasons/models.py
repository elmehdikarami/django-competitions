#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:40:44

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Season(models.Model):
    """
    A Tournament Season
    """
    name = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    tournament = models.ForeignKey('tournaments.Tournament', related_name='seasons')
    teams = models.ManyToManyField('teams.Team', related_name='seasons')
    enable_groups = models.BooleanField(default=True)
    won_points_home = models.IntegerField(default=3)
    won_points_away = models.IntegerField(default=3)
    draw_points_home = models.IntegerField(default=1)
    draw_points_away = models.IntegerField(default=1)
    lost_points_home = models.IntegerField(default=0)
    lost_points_away = models.IntegerField(default=0)
    table_view = models.OneToOneField('SeasonTableView', related_name='season')

    def __unicode__(self):
        return u'%s' % self.name


class SeasonTableView(models.Model):
    """
    Which informations to display 
    """
    team_emblem = models.BooleanField(default=True)
    nbr_played_games = models.BooleanField(default=True)
    nbr_wins = models.BooleanField(default=True)
    nbr_losts = models.BooleanField(default=True)
    nbr_points = models.BooleanField(default=True)
    win_percent = models.BooleanField(default=True)

# TODO : Add how to order teams if they have equal points..