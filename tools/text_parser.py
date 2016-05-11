#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: text_parser.py
@time: 16-3-18 下午10:27
"""


import json
import re

from copy import deepcopy


class TextParserQCWY(object):
    """
    文本解析工具(前程无忧)
    """
    def __init__(self, text_file_name=None, text_content=None):
        if text_file_name:
            self.file_lines = self.read_file_each_line(text_file_name)
        if text_content:
            self.file_lines = self.read_str_each_line(text_content)
        if text_file_name is None and text_content is None:
            raise Exception(u'未指定参数')

    @staticmethod
    def read_file_each_line(file_path):
        """
        逐行读取文件
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as f:
            for each_line in f:
                if isinstance(each_line, str):
                    each_line = each_line.decode('utf-8')
                yield each_line.strip(u'\r\n')

    @staticmethod
    def read_str_each_line(text_content):
        """
        逐行读取字符串
        :param text_content:
        :return:
        """
        if isinstance(text_content, str):
            text_content = text_content.decode('utf-8')
        for each_line in text_content.split(u'\n'):
            yield each_line

    @staticmethod
    def is_start(row_text):
        """
        正则检测是否是子选项开始
        :param row_text:
        :return:
        """
        title_rule = re.compile(ur'^(.*?)--(.*?)：(.*)$')
        title_result = re.match(title_rule, row_text)
        if not title_result:
            return False
        # print title_result.groups()
        return True

    @staticmethod
    def is_edu_title(row_text):
        """
        正则检测是否是教育经历title
        row_text = u'2002 /9--2005 /7 上海纺织工业大学 服装设计 大专'
        row_text = u'2002 /9--至今 上海纺织工业大学 服装设计 大专'
        :param row_text:
        :return:
        """
        edu_rule = re.compile(ur'^(.*?)--(.*) (.*?) (.*?) (.*?)$')
        edu_result = re.match(edu_rule, row_text)
        if not edu_result:
            return False
        # print edu_result.groups()
        return True

    def text_to_json(self):
        """
        解析文本文件
        :return:
        """
        from structures import Resume
        resume = Resume()
        resume_structure = resume
        resume_info = resume.data
        first = True                # 姓名第一行
        second = True               # 基本信息第二行
        has_recent_work = False     # 是否读取到最近工作经历
        last_key = None             # 上一个主节点
        current_key = None          # 当前主节点键
        current_sub_key = None      # 子节点
        current_item_dict = None
        current_line_index = 0  # 当前具体配置项目行数，下标起始１
        cycle_index = 0  # 循环次数
        structure_keys = resume_structure.data.keys()

        for file_line in self.file_lines:

            if file_line in structure_keys:
                current_key = file_line
                # print current_key

            # 处理字符串
            # 姓名第一个
            if first:
                resume_info[u'姓名'] = file_line
                first = False
                continue
            if second:
                base_info_list = [item.strip(u' ') for item in file_line.split(u' | ')]
                if len(base_info_list) >= 3:
                    resume_info[u'工龄'] = base_info_list[0]
                    resume_info[u'性别'] = base_info_list[1]
                    resume_info[u'出生日期'] = base_info_list[2]
                if len(base_info_list) >= 4:
                    resume_info[u'婚姻状况'] = base_info_list[3]
                if len(base_info_list) >= 5:
                    resume_info[u'身高'] = base_info_list[4]
                if len(base_info_list) >= 6:
                    resume_info[u'政治面貌'] = base_info_list[5]
                # print json.dumps(base_info_list, indent=4, ensure_ascii=False)
                second = False
                continue
            if file_line.startswith(u'居住地：'):
                resume_info[u'居住地'] = file_line.lstrip(u'居住地： ')
            if file_line.startswith(u'地　址：'):
                resume_info[u'地　址'] = file_line.lstrip(u'地　址： ')
            if file_line.startswith(u'电　话：'):
                resume_info[u'电　话'] = file_line.lstrip(u'电　话： ')
            if file_line.startswith(u'E-mail：'):
                resume_info[u'E-mail'] = file_line.lstrip(u'E-mail： ')
            if current_key in [u'自我评价']:
                if current_key == file_line:
                    continue
                resume_info[current_key] = file_line

            # 处理字典

            # 求职意向
            if current_key == u'求职意向':
                if file_line.startswith(u'到岗时间：'):
                    resume_info[current_key][u'到岗时间'] = file_line.lstrip(u'到岗时间： ')
                if file_line.startswith(u'工作性质：'):
                    resume_info[current_key][u'工作性质'] = file_line.lstrip(u'工作性质： ')
                if file_line.startswith(u'希望行业：'):
                    resume_info[current_key][u'希望行业'] = file_line.lstrip(u'希望行业： ')
                if file_line.startswith(u'目标地点：'):
                    resume_info[current_key][u'目标地点'] = file_line.lstrip(u'目标地点： ')
                if file_line.startswith(u'期望薪资：'):
                    resume_info[current_key][u'期望薪资'] = file_line.lstrip(u'期望薪资： ')
                if file_line.startswith(u'目标职能：'):
                    resume_info[current_key][u'目标职能'] = file_line.lstrip(u'目标职能： ')
                if file_line.startswith(u'求职状态：'):
                    resume_info[current_key][u'求职状态'] = file_line.lstrip(u'求职状态： ')

            # 最近工作
            if not has_recent_work:
                recent_work_rule = re.compile(ur'^最近工作\s\[.*\]')
                recent_work_result = re.match(recent_work_rule, file_line)
                if recent_work_result:
                    current_key = u'最近工作'
                    has_recent_work = True
                    continue
            if current_key == u'最近工作':
                if file_line.startswith(u'在岗时间：'):
                    resume_info[current_key][u'在岗时间'] = file_line.lstrip(u'在岗时间： ')
                if file_line.startswith(u'公　司：'):
                    resume_info[current_key][u'公　司'] = file_line.lstrip(u'公　司： ')
                if file_line.startswith(u'行　业：'):
                    resume_info[current_key][u'行　业'] = file_line.lstrip(u'行　业： ')
                if file_line.startswith(u'职　位：'):
                    resume_info[current_key][u'职　位'] = file_line.lstrip(u'职　位： ')

            # 列表项目

            # 工作经验
            if current_key == u'工作经验':
                # 当模块切换，清空计数器
                if last_key != u'工作经验':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    current_sub_key = None
                    cycle_index = 0
                    resume_info[current_key] = []
                    last_key = u'工作经验'
                if self.is_start(file_line):
                    # 初始化工作经验
                    current_item_dict = deepcopy(resume_structure.work_item)
                    rows = file_line.split(u'：')
                    current_item_dict[u'起止时间'] = rows[0]
                    current_item_dict[u'公司名称'] = rows[1]

                # 处理所属行业(部分没有行业字段)
                elif file_line.startswith(u'所属行业：'):
                    current_item_dict[u'所属行业'] = file_line.lstrip(u'所属行业： ')
                # 处理最后工作描述的换行
                elif current_line_index == 3*cycle_index and cycle_index > 0:
                    current_sub_key = u'工作描述'
                    current_item_dict[current_sub_key] = file_line
                else:
                    if current_sub_key:
                        # 处理最后责任描述内容的换行
                        # 因为读取到最后一个子项，结构已经封闭，需要从整体追加
                        resume_info[current_key][len(resume_info[current_key])-1][current_sub_key] += u'\n'+file_line
                        current_line_index -= 1
                # 判断单次循环是否结束
                if current_line_index == 3*cycle_index:
                    # print '='*8, file_line, current_sub_key, cycle_index
                    # print current_line_index, 3*cycle_index
                    if cycle_index > 0:
                        resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                    cycle_index += 1
                current_line_index += 1
                # print json.dumps(current_item_dict, indent=4, ensure_ascii=False)
                # print current_line_index, cycle_index
                continue

            # 项目经验
            if current_key == u'项目经验':
                # 当模块切换，清空计数器
                if last_key != u'项目经验':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    cycle_index = 0
                    current_sub_key = None
                    resume_info[current_key] = []
                    last_key = u'项目经验'
                if self.is_start(file_line):
                    # 初始化项目经验
                    current_item_dict = deepcopy(resume_structure.project_item)
                    rows = file_line.split(u'：')
                    current_item_dict[u'起止时间'] = rows[0]
                    current_item_dict[u'项目名称'] = rows[1]

                # 处理非必填项
                # 处理软件环境
                elif file_line.startswith(u'软件环境：'):
                    current_item_dict[u'软件环境'] = file_line.lstrip(u'软件环境： ')
                    current_sub_key = u'软件环境'
                    continue
                # 处理硬件环境
                elif file_line.startswith(u'硬件环境：'):
                    current_item_dict[u'硬件环境'] = file_line.lstrip(u'硬件环境： ')
                    current_sub_key = u'硬件环境'
                    continue
                # 处理开发工具
                elif file_line.startswith(u'开发工具：'):
                    current_item_dict[u'开发工具'] = file_line.lstrip(u'开发工具： ')
                    current_sub_key = u'开发工具'
                    continue

                # 处理必填项
                # 处理项目描述
                elif file_line.startswith(u'项目描述：'):
                    current_item_dict[u'项目描述'] = file_line.lstrip(u'项目描述： ')
                    current_sub_key = u'项目描述'
                # 处理责任描述
                elif file_line.startswith(u'责任描述：'):
                    current_item_dict[u'责任描述'] = file_line.lstrip(u'责任描述： ')
                    current_sub_key = u'责任描述'

                # 处理项目描述换行，直接追加
                elif current_sub_key == u'项目描述':
                    # print '-'*8, file_line, current_sub_key
                    current_item_dict[u'项目描述'] += u'\n'+file_line
                    current_line_index -= 1
                else:
                    # print '+'*8, file_line, current_sub_key
                    if current_sub_key:
                        # 处理最后责任描述内容的换行
                        # 因为读取到最后一个子项，结构已经封闭，需要从整体追加
                        print current_key, current_sub_key, file_line
                        resume_info[current_key][len(resume_info[current_key])-1][current_sub_key] += u'\n'+file_line
                        current_line_index -= 1

                # 判断单次循环是否结束
                if current_line_index == 3*cycle_index:
                    # print '='*8, file_line, current_sub_key
                    # print current_line_index, 3*cycle_index
                    if cycle_index > 0:
                        resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                    cycle_index += 1
                current_line_index += 1
                continue

            # 教育经历
            if current_key == u'教育经历':
                # 当模块切换，清空计数器
                if last_key != u'教育经历':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    current_sub_key = None
                    cycle_index = 0
                    resume_info[current_key] = []
                    last_key = u'教育经历'
                # 初始化教育经历
                edu_rule = re.compile(ur'^(.*?--.*)\s+(.*?)\s+(.*?)\s+(.*?)$')
                edu_result = re.match(edu_rule, file_line)
                if edu_result:
                    current_item_dict = deepcopy(resume_structure.edu_item)
                    rows = edu_result.groups()
                    current_item_dict[u'起止时间'] = rows[0]
                    current_item_dict[u'学校名称'] = rows[1]
                    current_item_dict[u'专业名称'] = rows[2]
                    current_item_dict[u'学历'] = rows[3]
                    resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                else:
                    continue

            # 培训经历
            if current_key == u'培训经历':
                # 培训经历
                # 当模块切换，清空计数器
                if last_key != u'培训经历':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    current_sub_key = None
                    cycle_index = 0
                    resume_info[current_key] = []
                    last_key = u'培训经历'
                # 初始化教育经历
                # 2012 /5--2013 /6：	连云港职业技术学院	电子CAD	电子CAD高级绘图员
                edu_rule = re.compile(ur'^(.*?--.*)：\s+(.*?)\s+(.*?)$')
                edu_result = re.match(edu_rule, file_line)
                if edu_result:
                    current_item_dict = deepcopy(resume_structure.train_item)
                    rows = edu_result.groups()
                    current_item_dict[u'起止时间'] = rows[0]
                    current_item_dict[u'培训机构'] = rows[1]
                    current_item_dict[u'培训项目'] = rows[2]
                    resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                else:
                    continue

            # 证书
            if current_key == u'证书':
                # 当模块切换，清空计数器
                if last_key != u'证书':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    current_sub_key = None
                    cycle_index = 0
                    resume_info[current_key] = []
                    last_key = u'证书'
                # 初始化证书
                cert_rule = re.compile(ur'^(\d{4}\s\/\d{1,2})\s+(.*?)$')
                cert_result = re.match(cert_rule, file_line)
                if cert_result:
                    current_item_dict = deepcopy(resume_structure.cert_item)
                    rows = cert_result.groups()
                    current_item_dict[u'发证时间'] = rows[0]
                    current_item_dict[u'证书名称'] = rows[1]
                    resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                else:
                    continue

            # IT 技能
            if current_key == u'IT 技能':
                # 当模块切换，清空计数器
                if last_key != u'IT 技能':
                    current_line_index = 0  # 当前具体配置项目行数，下标起始１
                    current_sub_key = None
                    cycle_index = 0
                    resume_info[current_key] = []
                    last_key = u'IT 技能'
                # 技能特殊处理，去掉标题行
                if file_line == u'技能名称 熟练程度 使用时间':
                    continue
                skill_rule = re.compile(ur'^(.*?) (.*?) (.*?)$')
                skill_result = re.match(skill_rule, file_line)
                if skill_result:
                    current_item_dict = deepcopy(resume_structure.skill_item)
                    rows = skill_result.groups()
                    current_item_dict[u'技能名称'] = rows[0]
                    current_item_dict[u'熟练程度'] = rows[1]
                    current_item_dict[u'使用时间'] = rows[2]
                    resume_info[current_key].append(current_item_dict)
                    current_item_dict = None
                else:
                    continue

        print json.dumps(resume_info, indent=4, ensure_ascii=False)


def test_read_str_each_line():
    text_parser = TextParserQCWY()
    text_test = u'''朱懿
5-7年工作经验 | 女 |  32岁（1983年7月22日） |  未婚 |  170cm
(ID:8841479)
居住地： 上海-浦东新区 户　口： 上海
地　址： 上海市浦东新区 （邮编：200127）
电　话： 13661669639（手机）'''
    text_lines = text_parser.read_str_each_line(text_test)
    for text_line in text_lines:
        print text_line


def test_text_to_json(text_file):
    """
    前程无忧文本简历解析测试
    :param text_file:
    :return:
    """
    text_parser = TextParserQCWY(text_file)
    text_parser.text_to_json()


if __name__ == '__main__':
    test_read_str_each_line()
