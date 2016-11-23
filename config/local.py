#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-18 下午10:10
"""


import os

CHROME_DRIVER_PATH = os.path.join(os.path.dirname(__file__), '../driver/chrome/mac64/chromedriver')

PROXY = "http://127.0.0.1:3128"  # IP:PORT or HOST:PORT


if __name__ == '__main__':
    print os.path.abspath(__file__)
    print CHROME_DRIVER_PATH
