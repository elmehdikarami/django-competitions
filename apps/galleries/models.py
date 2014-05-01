
# -*- coding: utf-8 -*-
"""
Created on Aug 23, 2013

@author: Mourad Mourafiq

@copyright: Copyright © 2013

Other contributers:
"""
import os
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from .utils import get_full_path_by_thumb


FULL = os.path.join(settings.MEDIA_ROOT, settings.IMAGES_STORE, 'full')
THUMBS = os.path.join(settings.MEDIA_ROOT, settings.THUMB_STORE)

logger = logging.getLogger(__name__)


class Gallery(models.Model):
    """
    Gallery object for a deal
    """
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        app_label = 'galleries'

    def __unicode__(self):
        return u'%s' % self.name


class Image(models.Model):
    """
    An Image model for a specific gallery, it represents an image with
    multiple thumbnails
    """
    url = models.URLField()
    picture = models.ImageField(upload_to=FULL, max_length=500)
    gallery = models.ForeignKey('Gallery', related_name='images')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        app_label = 'galleries'

    def __unicode__(self):
        return u'%s' % self.url


class Thumbnail(models.Model):
    """
    A Thumbnail model that represents a size which can be used to create
    thumbnail images
    """
    name = models.CharField(max_length=100, unique=True)
    height = models.IntegerField()
    width = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Thumbnail')
        verbose_name_plural = _('Thumbnails')
        app_label = 'galleries'

    def __unicode__(self):
        return u'%s' % self.name

    def to_url(self):
        return '%dx%d' % (self.width, self.height)

    def to_thumbnail(self):
        return self.height, self.width


@receiver(pre_delete, sender=Image)
def delete_image(sender, instance, **kwargs):
    for thumb in Thumbnail.objects.filter(is_active=True):
        try:
            os.remove(instance.picture)
            os.remove(get_full_path_by_thumb(thumb, instance))
        except Exception:
            pass
 

@receiver(pre_delete, sender=Gallery)
def delete_gallery(sender, instance, **kwargs):
    for image in instance.images.all():
        image.delete()
 