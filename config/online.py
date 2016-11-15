#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: online.py
@time: 16-3-18 下午10:10
"""


import os

CHROME_DRIVER_PATH = os.path.join(os.path.dirname(__file__), '../driver/chrome/linux64/chromedriver')


if __name__ == '__main__':
    print os.path.abspath(__file__)
    print CHROME_DRIVER_PATH
