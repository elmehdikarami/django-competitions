#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-03-30 23:26:09
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:18:06
from django.utils.translation import ugettext_lazy as _
from django.db import models


def upload_to_media():
    pass


class Tournament(models.Model):
    """
    Represents a Tournament sport
    """
    TEAM = '0'
    SINGLE = '1'
    PLAY_MODE_CHOICES = (
        (TEAM, _('Team')),
        (SINGLE, _('Single'))
        )
    name = models.CharField(_('Tournament name'), max_length=100)
    published = models.BooleanField(_('Whether or not the tournament is published'),default=True)
    logo = models.ImageField(upload_to=upload_to_media)
    play_mode = models.CharField(max_length=1, choices=PLAY_MODE_CHOICES, default=TEAM)
    about = models.TextField(
        blank=True,
        null=True,
        help_text=_('Some informations about the Tournament')
        )
