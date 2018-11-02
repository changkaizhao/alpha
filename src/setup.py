#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017, All rights reserved.
# Author: Hao Yan (yanhao.charles@gmail.com)

from pathlib import Path
from setuptools import setup

requirements = (Path(__file__).parent /'requirements.txt').read_text().strip().split()

setup(
    name='alpha',
    version='0.0.0',
    description='Alpha Project, A secret project!',
    url='https://github.com/changkaizhao/alpha',
    packages=['main', 'tic_tac_toe'],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['zyj_wx=zuoyeji.wechat_service.main:main']
    }
)
