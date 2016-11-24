#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_test.py
@time: 2016/11/23 下午9:41
"""


import unittest


test_modules = [
    'tests.test_bar.BarTest',
]

all_tests = [unittest.defaultTestLoader.loadTestsFromName(test_module) for test_module in test_modules]
test_suite = unittest.TestSuite(all_tests)
test_runner = unittest.TextTestRunner()
test_result = test_runner.run(test_suite)

# TODO 邮件发送结果
print '>>>'
print repr(test_result)
print test_result.testsRun

for e in test_result.errors:
    print 'err:------'
    for t in e:
        print str(t)
for e in test_result.failures:
    print 'failures: ------'
    for t in e:
        print str(t)

print '<<<'


# 将多个测试用例的结果统一打印
# python run_test.py
