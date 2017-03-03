#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bar_test.py
@time: 2016/11/23 下午10:34
"""


import unittest


class BarTest(unittest.TestCase):
    """
    单元测试例子
    ✗ python tests/bar_test.py
    """

    def setUp(self):
        self.bar = 'bar'
        self.foo = 'foo'

    def test_a(self):
        self.assertEqual(self.bar, self.foo)
        self.assertEqual(self.bar, self.bar)
        self.assertEqual(self.foo, self.foo)

    def test_b(self):
        self.assertGreater(self.bar, self.foo)

    def test_c(self):
        self.assertLess(self.bar, self.foo)

    def test_d(self):
        self.assertIn(self.bar, self.foo)

    def test_e(self):
        raise Exception(self.__doc__)

    def test_f(self):
        pass

    @unittest.skip("test skipping")
    def test_e(self):
        self.assertNotEqual('1', '2')

    def tearDown(self):
        self.bar = ''
        self.foo = ''


if __name__ == '__main__':
    # 方式一
    # unittest.main()

    # 方式二
    suite = unittest.TestLoader().loadTestsFromTestCase(BarTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    # todo 邮件发送测试结果

    print u'测试用例总数：', result.testsRun
    print u'错误总数：', len(result.errors)
    print u'失败总数：', len(result.failures)
    print u'跳过总数：', len(result.skipped)
    for e in result.errors:
        print 'err:------'
        for t in e:
            print str(t)
    for e in result.failures:
        print 'failures: ------'
        for t in e:
            print str(t)
