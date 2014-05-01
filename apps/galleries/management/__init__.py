#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-06 23:27:22
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:20
from django.db.models import signals

from apps.galleries.models import Thumbnail
import apps.galleries.models as galleries


def create_thumbnails(sender, **kwargs):
    Thumbnail.objects.get_or_create(name='tiny', width=300, height=150)


signals.post_syncdb.connect(create_thumbnails, sender=galleries, dispatch_uid='create_thumbnails_uid')
