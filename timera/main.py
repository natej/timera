# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import logging

try:
    # noinspection PyCompatibility
    from ConfigParser import SafeConfigParser as ConfigParser
except ImportError:
    # noinspection PyUnresolvedReferences
    from configparser import ConfigParser

log = logging.getLogger(__name__)


def reset_db(config, confirm=True):
    from .db import get_client
    from .db import reset
    idbc = get_client(config)
    reset(idbc, config, confirm=confirm)


def setup_env():
    """Remove env vars that may influence behavior.
    https://docs.python.org/2/library/os.html?highlight=os.environ#os.environ
    When unsetenv() is supported, deletion of items in os.environ is automatically translated
    into a corresponding call to unsetenv(); however, calls to unsetenv() don't update os.environ,
    so it is actually preferable to delete items of os.environ.
    Availability: most flavors of Unix, Windows.
    """
    keys = [ 'no_proxy', 'NO_PROXY', 'http_proxy', 'HTTP_PROXY', 'https_proxy', 'HTTPS_PROXY' ]
    for key in keys:
        if key in os.environ:
            del os.environ[key]


def parse_config(fname):
    # make sure we can read fname so we get an error now, since ConfigParser.read() doesn't
    with open(fname, 'r') as f:
        f.read()
    here = os.path.dirname(os.path.abspath(fname))
    defaults = dict(here=here)
    config = ConfigParser(defaults)
    config.read(fname)
    return config


def print_usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_filename> (start | reset_db)' % cmd)
    print('example: %s config.ini start' % cmd)


def get_args(argv):
    actions = ['start', 'reset_db']
    if len(argv) != 3 or argv[2] not in actions:
        print_usage(argv)
        raise ValueError('invalid arguments: %r' % argv)
    return argv
