#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:25:15
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:17
from django.contrib import admin

from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'nickname',
        'team', 'position', 'is_captain', 'city'
        )


admin.site.register(Player, PlayerAdmin)
