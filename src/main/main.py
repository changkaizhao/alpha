#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018, Alpha Inc. All rights reserved.
# Author: XXX

"""
main module
"""
"""
口算作业批改 服务入口
"""

import json
import os
import logging
import logging.config
import yaml

import tornado.ioloop
import tornado.web
from tornado.options import options, parse_config_file

from main.handlers import MainHandler

from tic_tac_toe.config import settings
from tic_tac_toe.game_manager import TicTacToeGameManager
from tic_tac_toe.handlers import IndexHandler, TicTacToeHandler, TicTacToeSocketHandler


CONFIG_PATH = ''
DEV_MODE = True
LOGGER_MODULE_NAME = '{0: <{width}}'.format('main', width=14)


def normal_response(data):
    return {"error": None, "data": data}

def make_app():
    tic_tac_toe_game_manager = TicTacToeGameManager()

    return tornado.web.Application([
        # (r"/", MainHandler),
        (r"/$", IndexHandler),
        (r"/tic-tac-toe$", TicTacToeHandler),
        (r"/tic-tac-toe/ws$", TicTacToeSocketHandler,
         dict(game_manager=tic_tac_toe_game_manager))
    ], debug=DEV_MODE)


def get_config_path():
    if DEV_MODE:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "app_conf.py")
    else:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "prod_app_conf.py")


if __name__ == "__main__":
    if DEV_MODE:
        log_conf_name = 'log_conf_dev.yaml'
    else:
        log_conf_name = 'log_conf.yaml'

    logging_config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_conf_name)
    logging.config.dictConfig(yaml.load(open(logging_config_path, 'r')))
    logger = logging.getLogger(LOGGER_MODULE_NAME)
    parse_config_file(get_config_path())
    logger.info("START APP!")
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
