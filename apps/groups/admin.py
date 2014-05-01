#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-06 23:57:17
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:20
from django.contrib import admin

from .models import Group


class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('teams', )


admin.site.register(Group, GroupAdmin)
