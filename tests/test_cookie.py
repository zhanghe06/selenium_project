#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_cookie.py
@time: 2017/1/10 上午12:58
"""


import json
import sys
sys.path.append('..')

from config import CHROME_DRIVER_PATH
from selenium import webdriver

resume_link = 'http://www.51job.com'

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(resume_link)
print driver.title
print json.dumps(driver.get_cookies(), ensure_ascii=False, indent=4)
driver.close()


if __name__ == '__main__':
    pass


"""
[
    {
        "domain": ".51job.com",
        "secure": false,
        "value": "indexguide%3D1",
        "expiry": 1518536136.501206,
        "path": "/",
        "httpOnly": false,
        "name": "slife"
    },
    {
        "domain": ".51job.com",
        "name": "51job",
        "value": "cenglish%3D0",
        "path": "/",
        "httpOnly": false,
        "secure": false
    },
    {
        "domain": ".51job.com",
        "secure": false,
        "value": "14870001354967150029",
        "expiry": 1798040136.500014,
        "path": "/",
        "httpOnly": false,
        "name": "guid"
    }
]
"""