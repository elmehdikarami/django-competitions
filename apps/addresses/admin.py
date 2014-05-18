#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-06 23:51:55
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-18 02:10:14
from django.contrib import admin

from .models import Country, City


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'country', 'slug')
    search_fields = ('name', 'country__name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
