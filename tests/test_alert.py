#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_alert.py
@time: 16-5-11 下午12:23
"""

import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


resume_link = 'http://localhost:63342/selenium_project/tests/alert.html'

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(resume_link)

try:
    alert_text = Alert(driver).text
    print alert_text
    Alert(driver).accept()
    print driver.title
except NoAlertPresentException as e:
    print u'没有弹窗'

driver.close()


if __name__ == '__main__':
    pass
