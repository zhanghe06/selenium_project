#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: text_parser.py
@time: 16-3-18 下午10:27
"""


import json


class TextParser(object):
    """
    文本解析工具
    """
    def __init__(self):
        pass


class Position(object):
    """
    职位数据结构
    """
    # 职位整体结构
    data = {
        # 基本信息
        u'工龄': u'',  # 10年以上工作经验 应届毕业生 1年工作经验
        u'性别': u'',
        u'年龄': u'',
        u'出生日期': u'',
        u'婚姻状况': u'',
        u'身高': u'',
        u'居住地': u'',
        u'地　址': u'',
        u'电　话': u'',
        u'E-mail': u'',
        # 当前信息
        u'最近工作': {
            u'在岗时间': u'',  # [ 2 年7个月] [ 5个月] [ 应届生简历/无工作经验 ]
            u'公　司': u'',
            u'行　业': u'',
            u'职　位': u''
        },
        u'学历': {
            u'学　历': u'',
            u'专　业': u'',
            u'学　校': u''
        },
        # 目前工资
        u'目前工资': {
            u'目前薪资': u'',
            u'基本工资': u'',
            u'补贴/津贴': u'',
            u'奖金/佣金': u''
        },
        # 详细信息
        u'自我评价': u'',
        u'求职意向': {
            u'到岗时间': u'',
            u'工作性质': u'',
            u'希望行业': u'',
            u'目标地点': u'',
            u'期望薪资': u'',
            u'目标职能': u'',
            u'求职状态': u'',
        },
        u'工作经验': [],
        u'教育经历': [],
        u'所获奖项': [],
        u'学生实践经验': [],
        u'校内职务': [],
        u'培训经历': [],
        u'证书': [],
        u'语言能力': [],
        u'IT 技能': [],
        u'其他信息': []
    }

    # 工作经验
    work_item = {
        u'起止时间': u'',
        u'公司名称': u'',
        u'所属行业': u'',
        u'部门': u'',
        u'岗位名称': u'',
        u'工作描述': u''
    }

    # 教育经历
    edu_item = {
        u'起止时间': u'',
        u'学校名称': u'',
        u'专业名称': u'',
        u'学历': u'',
        u'岗位名称': u'',
        u'工作描述': u''
    }

    # 培训经历
    train_item = {
        u'起止时间': u'',
        u'培训机构': u'',
        u'培训项目': u'',
        u'培训内容': u''
    }

    # 证书
    cert_item = {
        u'发证时间': u'',
        u'证书名称': u''
    }

    # IT 技能
    skill_item = {
        u'技能名称': u'',
        u'熟练程度': u'',
        u'使用时间': u''
    }


def test_position():
    """
    职位测试
    :return:
    """
    # 实例化职位结构
    position = Position()

    # 添加工作经历
    work_item_01 = {
        u'起止时间': u'',
        u'公司名称': u'',
        u'所属行业': u'',
        u'部门': u'',
        u'岗位名称': u'',
        u'工作描述': u''
    }
    work_item_02 = {
        u'起止时间': u'',
        u'公司名称': u'',
        u'所属行业': u'',
        u'部门': u'',
        u'岗位名称': u'',
        u'工作描述': u''
    }
    position.data[u'工作经验'].append(work_item_01)
    position.data[u'工作经验'].append(work_item_02)

    # 添加教育经历
    edu_item_01 = {
        u'起止时间': u'',
        u'学校名称': u'',
        u'专业名称': u'',
        u'学历': u'',
        u'岗位名称': u'',
        u'工作描述': u''
    }
    position.data[u'教育经历'].append(edu_item_01)

    # 添加培训经历
    train_item_01 = {
        u'起止时间': u'',
        u'培训机构': u'',
        u'培训项目': u'',
        u'培训内容': u''
    }
    position.data[u'培训经历'].append(train_item_01)

    # 数据职位信息
    print json.dumps(position.data, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    test_position()
