#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_remote.py
@time: 2017/1/6 上午12:47
"""


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
)

test_link = 'http://www.baidu.com'

driver.get(test_link)
print driver.title

# NoSuchElementException
# ele_not_exit = driver.find_element_by_id('not_exit')

driver.quit()


if __name__ == '__main__':
    pass
