#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_simple.py
@time: 16-5-11 下午1:15
"""


import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver

resume_link = 'http://www.51job.com'

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(resume_link)
print driver.title
driver.close()


if __name__ == '__main__':
    pass
