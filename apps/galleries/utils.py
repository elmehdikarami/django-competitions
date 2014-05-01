#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-04-06 23:21:41
# @Last Modified by:   karami
# @Last Modified time: 2014-04-06 23:21:43
# -*- coding: utf-8 -*-
from django.conf import settings

import os


def get_url_by_thumb(thumb, image):
    """
    Returns the url of a given image
    """
    filename = image.picture.name.split('/')[-1]
    return os.path.join(settings.MEDIA_URL, settings.THUMB_STORE,thumb.name, filename)


def get_full_path_by_thumb(thumb, image):
    """
    Returns the full absolute path of thumbnail's image
    """
    filename = image.picture.name.split('/')[-1]
    return os.path.join(settings.MEDIA_ROOT, settings.THUMB_STORE, thumb.name, filename)
