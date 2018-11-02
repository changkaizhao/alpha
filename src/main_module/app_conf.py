#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2018, Alpha Inc. All rights reserved.
# Author: XXX

"""
模型服务常量
"""
from tornado.options import define

define("port", default=8888, help="服务运行端口")


#========================================#
#              mysql 配置项              #
#========================================#
define("db_user_name", default='root', help="数据库用户名")
define("db_password", default='sqlPass@zuoyeji', help="数据库密码")
define("db_address", default='localhost', help="数据库地址")
define("db_port", default=8806, help="数据库端口")
define("db_name", default='KouSuanDB', help="数据库名字")
define("db_sql_name", default="mysql", help="数据库类型名称")
define("db_sql_api", default='pymysql', help="数据库python API 库")
define("db_charset", default='utf8mb4', help="数据库字符集类型")
define("db_debug_model", default=True, help="数据库使用模式")
define("db_pool_recycle", default=3600, help="由于MySQL 会在一定时间自动关闭连接，需要数据库连接池的连接对象在一定时间（秒内）更新为新连接 以保持连接持续存在")
define("db_pool_size", default=100, help="连接池容量")
