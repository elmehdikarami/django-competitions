#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Karami El Mehdi
# @Date:   2014-05-01 00:11:49
# @Last Modified by:   elmehdikarami
# @Last Modified time: 2014-05-01 00:47:21
TEST_INSTALLED_APPS = (
	'django_jenkins',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8'
)
