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
PROXY_HOST = '192.168.2.158'
PROXY_PORT = 3128
PROXY = 'http://%s:%s' % (PROXY_HOST, PROXY_PORT)


def test_chrome():
    """
    测试 Chrome
    :return:
    """
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


def test_firefox():
    """
    测试 Firefox
    :return:
    """
    # Only used if Firefox is requested.
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)

    # 代理配置
    profile.set_preference('network.proxy.http', PROXY_HOST)
    profile.set_preference('network.proxy.http_port', PROXY_PORT)
    profile.set_preference('network.proxy.ssl', PROXY_HOST)
    profile.set_preference('network.proxy.ssl_port', PROXY_PORT)
    profile.set_preference('network.proxy.type', 1)

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX,
        browser_profile=profile,
    )

    test_link = 'http://www.baidu.com'

    driver.get(test_link)
    print driver.title
    # driver.quit()


if __name__ == '__main__':
    test_chrome()
    # test_firefox()
