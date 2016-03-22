#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 16-3-21 上午10:32
"""

from urlparse import urlparse, parse_qs


def get_url_param_value(url, param_key):
    """
    获取链接查询参数值
    :param url:
    :param param_key:
    :return:
    """
    result = urlparse(url)
    params = parse_qs(result.query, True)
    param_value = params.get(param_key)
    print result, '\n', params, '\n', param_value
    return ','.join(param_value)


def test():
    """
    测试
    :return:
    """
    url = 'http://ehire.51job.com/Candidate/ResumeViewFolder.aspx?hidSeqID=7691229674&hidFolder=EMP&hidFolder=EMP2'
    hidSeqID = get_url_param_value(url, 'hidSeqID')
    print hidSeqID
    hidFolder = get_url_param_value(url, 'hidFolder')
    print hidFolder


if __name__ == '__main__':
    test()
