#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:27:33
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:15
from django.contrib import admin

from .models import Position


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Position, PositionAdmin)
