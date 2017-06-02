# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import io
import re

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf-8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('unable to find version string')


setup(
    name='timera',
    version=find_version('timera', '__init__.py'),
    description='Store stats in InfluxDB.',
    long_description=read('README.rst'),
    author='Nathan Jennings',
    url='https://github.com/natej/timera',
    license=read('LICENSE.txt'),
    packages=find_packages(exclude=('.cache', 'contrib', 'docs', 'tests'))
)
