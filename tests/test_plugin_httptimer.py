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


def get_run_items(config, plugin_type):
    run_items = []
    run_list = timera.collector.get_run_list(config)
    for item in run_list:
        if item['type'] != plugin_type:
            continue
        run_items.append(item)
    return run_items


def test_get_url():
    config = get_config()
    reset_db(config)
    idbc = timera.db.get_client(config)
    timestamp = timera.util.get_unix_now()
    run_items = get_run_items(config, 'httptimer')
    assert run_items
    for plugin in run_items:
        proxy = plugin['config'].get('proxy')
        include_direct = timera.util.asbool(plugin['config'].get('include_direct'))
        if not proxy or include_direct:
            # get stats using direct connection
            stats_direct = timera.plugins.httptimer.get_url(config, timestamp, plugin, None)
            timera.plugins.httptimer.write_stats(idbc, stats_direct)
        if proxy:
            # get stats using proxy
            stats_proxy = timera.plugins.httptimer.get_url(config, timestamp, plugin, proxy)
            timera.plugins.httptimer.write_stats(idbc, stats_proxy)
    # make sure socket is closed
    idbc._session.close()
