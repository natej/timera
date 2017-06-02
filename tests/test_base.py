# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import timera

dirname = os.path.dirname(os.path.abspath(__file__))


def get_config_fname():
    return os.path.join(dirname, 'config.ini')


def get_config():
    config = timera.main.parse_config(get_config_fname())
    return config


def reset_db(config):
    timera.main.reset_db(config, confirm=False)


def test_get_config():
    config = get_config()
    assert config


def test_db_reset():
    config = get_config()
    reset_db(config)


def test_db_write_points():
    config = get_config()
    reset_db(config)
    idbc = timera.db.get_client(config)
    md = dict(measurement='m1', fields=dict(value=str(0.42)))
    timera.db.write_points(idbc, [md])
    # make sure socket is closed
    idbc._session.close()
