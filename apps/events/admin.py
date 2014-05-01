#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-06 23:57:17
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:19:07
from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'player_event', 'player', 'team')


admin.site.register(Event, EventAdmin)
