#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_web.py
@time: 2016/11/22 上午10:52
"""


import unittest
import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH, PROXY
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)

    def test_get_page_title(self):
        url_link = 'https://www.s2c.wealink.com/index/need'
        self.driver.get(url_link)
        web_title = self.driver.title
        # print web_title, type(web_title)
        self.assertEqual(web_title, u'8公里 - 找同城服务，解决您的一切生活问题', u'测试失败')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
