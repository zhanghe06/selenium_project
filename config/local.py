#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-18 下午10:10
"""


import os
import platform


# TODO windows
SYSTEM_DICT = {
    'Linux': 'linux',
    'Darwin': 'mac'
}

MACHINE_DICT = {
    'i686': '32',
    'x86_64': '64'
}

SYSTEM_ENV = platform.system()

MACHINE_ENV = platform.machine()

DRIVER_ENV = SYSTEM_DICT.get(SYSTEM_ENV) + MACHINE_DICT.get(MACHINE_ENV)

CHROME_DRIVER_PATH = os.path.join(os.path.dirname(__file__), '../driver/chrome/%s/chromedriver' % DRIVER_ENV)

PROXY = "http://127.0.0.1:3128"  # IP:PORT or HOST:PORT


if __name__ == '__main__':
    print os.path.abspath(__file__)
    print CHROME_DRIVER_PATH
    print MACHINE_ENV
    print SYSTEM_ENV
    print DRIVER_ENV
