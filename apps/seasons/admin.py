#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:31:26
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:14
from django.contrib import admin

from .models import Season, SeasonTableView


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'published', 'enable_groups')


class SeasonTableViewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Season, SeasonAdmin)
admin.site.register(SeasonTableView, SeasonTableViewAdmin)
