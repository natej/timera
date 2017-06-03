#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import logging

import timera

log = logging.getLogger()


def setup_log(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(threadName)-9s %(message)s')
    sh.setFormatter(formatter)
    log.addHandler(sh)
    log.setLevel(log_level)


def main(argv):
    try:
        cmd, config_fname, action = timera.main.get_args(argv)
    except timera.exc.TimeraInvalidArgs:
        return
    config = timera.main.parse_config(config_fname)
    if action == 'reset_db':
        timera.main.reset_db(config)
        return
    debug = timera.util.asbool(config.get('main', 'debug'))
    setup_log(debug)
    timera.main.setup_env()
    timera.collector.run_loop(config)


if __name__ == '__main__':
    main(sys.argv)
