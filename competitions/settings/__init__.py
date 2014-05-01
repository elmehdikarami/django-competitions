#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-05-01 00:10:25
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 12:17:47
from .settings import *
from .local import SECRET_KEY

try:
    from .prod import *
    INSTALLED_APPS += PROD_INSTALLED_APPS
except ImportError:
    pass

try:
    from .dev import *
except ImportError:
    pass

if 'test' in sys.argv or 'jenkins' in sys.argv:
    try:
        from .test import *
        INSTALLED_APPS += TEST_INSTALLED_APPS
    except ImportError:
        pass
