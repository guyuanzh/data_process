#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
from xlwt import Workbook

import common


def process_da001_and_da002(data):
    t1 = str('4')
    t2 = str('5')
    s1 = str(data[3])
    s2 = str(data[4])

    if s1 == '' and s2 == '':
        return ''
    if s1 != '':
        if t1 in s1 or t2 in s1:
            return '1'
        else:
            return '0'

    if s2 != '':
        if t1 in s2 or t2 in s2:
            return '1'
        else:
            return '0'


def process_da007(data):
    tmp = data[5:19]

    if '' in tmp:
        return ''
    if '1 Yes' in tmp:
        return 1
    else:
        return 0


def process_db(data):
    tmp = data[19:28]
    if '4 I Can' in tmp:
        return 1
    if '3 Yes, I' in tmp:
        return 1
    else:
        return 0


def util_db(arr):
    if '4 I Can' == arr:
        return 1
    if '3 Yes, I' == arr:
        return 1
    else:
        return 0


def util_da007(arr):
    if '' in arr:
        return ''
    if '1 Yes' in arr:
        return 1
    else:
        return 0


def util_da(s):
    if s[0] == '4' or s[0] == '5':
        return 1
    if s == '':
        return ''
    else:
        return 0


def f(d):
    tmp1 = d[0:3]
    tmp2 = process_da001_and_da002(d)
    tmp3 = process_da007(d)
    tmp4 = process_db(d)
    tmp1.append(tmp2)
    tmp1.append(tmp3)
    tmp1.append(tmp4)
    return tmp1


def process_excel_data(data):
    # type: (object) -> object
    tmp = []
    for index in range(1, len(data)):
        d = data[index]
        tmp1 = f(d)
        tmp.append(tmp1)
    return tmp


def process_excel_w(data):
    work_book = xlwt.Workbook(style_compression=2)  # type: Workbook
    # 创建sheet1
    sheet1 = work_book.add_sheet(u'sheet1', cell_overwrite_ok=True)
    row0 = [u'ID', u'householdID', u'communityID', u'srh', u'chronic', u'adl']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], common.set_excel_style('Times New Roman', 220, True))
    count = 1
    for row in data:
        for i in range(0, len(row)):
            sheet1.write(count, i, row[i], common.set_excel_style('Times New Roman', 220, True))
        count = count + 1
    work_book.save('/Users/zhangguyuan/Documents/result/file01.xlsx')
