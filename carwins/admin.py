#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: admin.py
@time: 16-6-16 下午10:01
"""


import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ipdb


login_link = 'http://v4.manage.carwins.cn/Login'
root_link = 'http://v4.manage.carwins.cn/'

login_info = {
    'username': u'褚建利',
    'password': '111111'
}

# 登陆
# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(login_link)
cookie = driver.get_cookies()
print cookie
print driver.title

elem_username = driver.find_element(By.XPATH, '//input[@placeholder="用户名"]')
elem_password = driver.find_element(By.XPATH, '//input[@placeholder="密码"]')
elem_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')

elem_username.clear()
elem_username.send_keys(login_info['username'])
elem_password.clear()
elem_password.send_keys(login_info['password'])
elem_submit.send_keys(Keys.RETURN)


# 进入管理页面
driver.get(root_link)
cookie = driver.get_cookies()
print cookie
ipdb.set_trace()
print driver.title


# 采购线索管理
elem_cgxs = driver.find_element(By.XPATH, '//a[text()="采购线索管理"]')
cgxs_link = elem_cgxs.get_attribute('href')
print cgxs_link  # u'http://v4.manage.carwins.cn/potentialbuyseller/potentialgsellerlist'
driver.find_element_by_partial_link_text(u'采购线索管理')

if __name__ == '__main__':
    pass
