#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_wait.py
@time: 2017/3/3 上午9:33
"""


import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver

resume_link = 'http://www.51job.com'

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# 隐式等待10秒
driver.implicitly_wait(10)  # seconds
driver.get(resume_link)
print driver.title
driver.close()


if __name__ == '__main__':
    pass
