#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_proxy.py
@time: 16-4-12 下午2:27
"""


import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver


PROXY = "http://192.168.2.158:3128"  # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
chrome.get("http://ip.cn")


if __name__ == '__main__':
    pass
