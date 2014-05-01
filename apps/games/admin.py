#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:18:32
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:42:19
from django.contrib import admin

from .models import Game, GameDetail


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team_home', 'team_away', 'date', 'score_home',
        'score_away', 'playoff', 'played', 'season', 'duration'
        )


class GameDetailAdmin(admin.ModelAdmin):
    list_display = ('Game', 'manually_points', 'city')
    filter_horizontal = ('events',)


admin.site.register(Game, GameAdmin)
admin.site.register(GameDetail, GameDetailAdmin)
