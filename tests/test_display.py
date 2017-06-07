#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_display.py
@time: 16-6-20 下午9:08
"""


from pyvirtualdisplay import Display
from selenium import webdriver
import sys
sys.path.append('..')
from config import CHROME_DRIVER_PATH


test_link = 'http://www.baidu.com'

display = Display(visible=False, size=(800, 600))  # 依赖Xvfb
# display = Display(visible=True, size=(800, 600))  # 依赖Xephyr
display.start()

# now Chrome will run in a virtual display.
# you will not see the browser.
browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
browser.get(test_link)
print browser.title
browser.quit()

display.stop()
