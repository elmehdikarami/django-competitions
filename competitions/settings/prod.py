#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-05-01 00:11:45
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:52:50
PROD_INSTALLED_APPS = (
    'apps.addresses',
    'apps.events',
    'apps.groups',
    'apps.games',
    'apps.players',
    'apps.positions',
    'apps.seasons',
    'apps.tournaments',
    'apps.teams',
    'apps.galleries',
)

THIRD_PARTY_APPS = (
    'south',
)

SOUTH_TESTS_MIGRATE = False

PROD_INSTALLED_APPS += THIRD_PARTY_APPS
