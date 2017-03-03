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
from selenium.webdriver.common.proxy import Proxy


# PROXY = 'http://127.0.0.1:3128'
PROXY = 'http://192.168.2.158:3128'

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME,
    proxy=Proxy({
        "httpProxy": PROXY,
        "sslProxy": PROXY
    })
)

test_link = 'http://www.baidu.com'

driver.get(test_link)
print driver.title
driver.quit()


if __name__ == '__main__':
    pass
