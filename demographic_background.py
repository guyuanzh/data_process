#!/usr/bin/env python
# -*- coding: utf-8 -*-
import common
import xlwt


def process_ba000_w2_3(data):
    p_data = data[3]
    if p_data == '1 male':
        return 1
    else:
        return 0


def process_be001(data):
    p_data = data[4]

    if p_data == '3Separa':
        return 1
    else:
        return 0


def process_be002(data):
    p_data = data[5]

    if p_data == '5Widowe':
        return 1
    else:
        return 0


def process_bc001_w3_1(data):
    p_data = data[6]

    if p_data == '1 yes':
        return 1
    else:
        return 0


def process_bd001_w2_4(data):
    p_data = data[7]

    if p_data == '6High S' or p_data == '7Vocati' or p_data == '8 Two/Th' or p_data == '9 Four-y' or p_data == '10master' or p_data == '11doctor':
        return 1
    else:
        return 0


def process_ba004_w3_1(data):
    p_data = data[8]

    if p_data == '':
        return ''
    else:
        return 2019 - p_data


def my_sort(data):
    data.sort(
        key=lambda l: (l[2], l[1], l[0])
    )

    return data


def util(data):
    tmp1 = data[0:3]
    tmp2 = process_ba000_w2_3(data)
    tmp3 = process_be001(data)
    tmp4 = process_be002(data)
    tmp5 = process_bc001_w3_1(data)
    tmp6 = process_bd001_w2_4(data)
    tmp7 = process_ba004_w3_1(data)

    tmp1.append(tmp2)
    tmp1.append(tmp3)
    tmp1.append(tmp4)
    tmp1.append(tmp5)
    tmp1.append(tmp6)
    tmp1.append(tmp7)

    return tmp1


def process_excel_data(data):
    tmp = []
    for index in range(1, len(data)):
        d = data[index]
        tmp1 = util(d)
        tmp.append(tmp1)
    return tmp


def process_excel_w(data):
    work_book = xlwt.Workbook(style_compression=2)  # type: Workbook
    # 创建sheet1
    sheet1 = work_book.add_sheet(u'sheet1', cell_overwrite_ok=True)
    row0 = [u'ID', u'householdID', u'communityID', u'male', u'sep', u'widow', u'hukou', u'ms', u'age']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], common.set_excel_style('Times New Roman', 220, True))
    count = 1
    for row in data:
        for i in range(0, len(row)):
            sheet1.write(count, i, row[i], common.set_excel_style('Times New Roman', 220, True))
        count = count + 1
    work_book.save('/Users/zhangguyuan/Downloads/result/Demographic_Background.xlsx')
