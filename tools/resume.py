#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: resume.py
@time: 16-3-21 上午8:55
"""


from selenium import webdriver
from url import get_url_param_value
import time

import os


def read_dir_files(root_dir, suffix=None):
    """
    遍历读取指定目录下文件名称
    :param root_dir:
    :param suffix: None / '.html'
    :return:
    """
    file_list = [file_name for file_name in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, file_name))]
    if suffix:
        file_list = [item for item in file_list if item.endswith(suffix)]
    for file_name in file_list:
        # 返回文件名称(不包含路径)
        yield file_name
        # 返回文件内容
        # file_path = os.path.join(root_dir, file_name)
        # print file_path
        # with open(file_path, 'r') as f:
        #     html = f.read()
        #     yield html


def save_resume_html_to_text(driver_obj, resume_link, save_dir):
    """
    读取简历详情单页，并保存文件为文本文件
    :param driver_obj:
    :param resume_link:
    :param save_dir:
    :return:
    """
    driver_obj.get(resume_link)
    print driver_obj.title
    resume_base = driver_obj.find_element_by_xpath('//table[@id="divResume"]//table//table//table[1]')
    resume_current = driver_obj.find_element_by_xpath('//table[@id="divResume"]//table//table//table[2]')
    resume_detail = driver_obj.find_element_by_xpath('//table[@id="divResume"]//table//table//table[3]')
    resume_info = u'\n'.join([resume_base.text, resume_current.text, resume_detail.text]).encode('utf-8')

    print type(resume_info), resume_info

    # apply_id = get_url_param_value(resume_link, 'hidSeqID')
    file_name = os.path.join(save_dir, '%s_%s.txt' % (driver_obj.title, time.time()))
    with open(file_name, 'w') as f:
        f.write(resume_info)
    # driver_obj.close()


def test_save_resume_html_to_text():
    driver = webdriver.Firefox()
    resume_url = 'http://localhost:63342/selenium_project/test/html/朱懿.html'
    save_dir = '/home/zhanghe/code/selenium_project/test/text'
    save_resume_html_to_text(driver, resume_url, save_dir)


def test_read_dir_files():
    root_dir = '/home/zhanghe/code/wealink/hr/src/tpl/51job/resume'
    read_dir_files(root_dir)


def test_html_to_text():
    """
    指定目录下的所有html文件提取出文本并保存
    :return:
    """
    root_dir = '/home/zhanghe/code/wealink/hr/src/tpl/51job/resume'
    save_dir = '/home/zhanghe/code/wealink/hr/src/tpl/51job/resume/text'
    driver = webdriver.Firefox()
    file_names = read_dir_files(root_dir, 'html')
    for file_name in file_names:
        url = 'http://localhost:63342/hr/tpl/51job/resume/%s' % file_name
        save_resume_html_to_text(driver, url, save_dir)
    driver.quit()


def test_text_to_json():
    """
    读取指定目录下的所有文本文件，并输出json
    :return:
    """
    from text_parser import TextParserQCWY
    root_dir = '/home/zhanghe/code/wealink/hr/src/tpl/51job/resume/text'
    file_names = read_dir_files(root_dir, 'txt')

    for file_name in file_names:
        print '-'*20, file_name
        text_parser = TextParserQCWY(os.path.join(root_dir, file_name))
        text_parser.text_to_json()


def test_text_to_json_one():
    """
    读取指定单个文本文件，并输出json
    :return:
    """
    from text_parser import TextParserQCWY
    file_name = '/home/zhanghe/code/wealink/hr/src/tpl/51job/resume/text/郑祖清_1458631707.64.txt'
    text_parser = TextParserQCWY(file_name)
    text_parser.text_to_json()


if __name__ == '__main__':
    # test_html_to_text()
    test_text_to_json()
    # test_text_to_json_one()
