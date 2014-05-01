#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:37:26
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:08
from django.contrib import admin

from .models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'play_mode', 'published')


admin.site.register(Tournament, TournamentAdmin)
