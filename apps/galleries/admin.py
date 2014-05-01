#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-07 00:13:18
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:19:07
from django.contrib import admin

from .models import Gallery, Image, Thumbnail


class GalleryAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

class ThumbnailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)
