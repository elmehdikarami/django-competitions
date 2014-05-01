#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:35:33
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:12
from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_on')


admin.site.register(Team, TeamAdmin)
