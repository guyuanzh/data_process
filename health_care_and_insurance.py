#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import common
import xlwt


def process_ed010(data):
    p_data = data[3]
    if p_data == 1 or p_data == 2 or p_data == 3 or p_data == 4:
        return 1
    else:
        return 0


def process_ed001(data):
    p_data = data[4]
    if p_data == 2:
        return 0
    else:
        return p_data


def process_ed023_1(data):
    p_data = data[5]
    if p_data != '':
        return math.log(p_data)
    else:
        return 0


def process_ed024_1(data):
    p_data = data[6]
    if p_data != '':
        return math.log(p_data)
    else:
        return 0


def process_ed023_1_ed024_1(data):
    p_data1 = data[5]
    p_data2 = data[6]

    if p_data1 == '':
        return 0
    else:
        return p_data1 / p_data2


def process_ed002(data):
    p_data = data[7]
    if p_data == '2':
        return '0'
    else:
        return p_data


def process_ee003(data):
    p_data = data[8]
    if p_data == '2':
        return 0
    else:
        return p_data


def process_ee024_eeo25_ee026(data):
    p_data1 = data[9]
    p_data2 = data[10]
    p_data3 = data[11]

    print type(p_data2)

    if p_data1 == '':
        p_data1 = 0
    elif p_data2 == '':
        p_data2 = 0
    elif p_data3 == '':
        p_data3 = 0

    res = p_data1+p_data2+p_data3
    if res == 0:
        return 0
    else:
        math.log(res)


def process_ee027_1(data):
    p_data = data[12]

    if p_data == '':
        return 0
    else:
        return math.log(p_data)


def process_10(data):
    p_data1 = process_ee027_1(data)
    p_data2 = process_ee024_eeo25_ee026(data)

    if p_data2 == '':
        return 0
    else:
        return p_data1 / p_data2


def process_11(data):
    p_data1 = data[13]
    p_data2 = data[14]
    p_data3 = data[15]
    p_data4 = data[16]
    p_data5 = data[17]
    p_data6 = data[18]
    p_data7 = data[19]

    if p_data7 == '':
        return 0
    elif p_data1 == '' and p_data2 == '' and p_data3 == '' and p_data4 == '' and p_data5 == '' and p_data6 == '' and p_data7 == '':
        return ''
    else:
        return 1


def process_12(data):
    p_data1 = data[20]
    p_data2 = data[21]
    p_data3 = data[22]
    p_data4 = data[23]
    p_data5 = data[24]
    p_data6 = data[25]

    if p_data1 == '':
        p_data1 = 0
    elif p_data2 == '':
        p_data2 = 0
    elif p_data3 == '':
        p_data3 = 0
    elif p_data4 == '':
        p_data4 = 0
    elif p_data5 == '':
        p_data5 = 0
    elif p_data6 == '':
        p_data6 = 0

    return p_data1+p_data2+p_data3+p_data4+p_data5+p_data6


def process_13(data):
    p_data1 = data[26]
    p_data2 = data[27]
    p_data3 = data[28]
    p_data4 = data[29]
    p_data5 = data[30]
    p_data6 = data[31]

    if p_data1 == '':
        p_data1 = 0
    elif p_data2 == '':
        p_data2 = 0
    elif p_data3 == '':
        p_data3 = 0
    elif p_data4 == '':
        p_data4 = 0
    elif p_data5 == '':
        p_data5 = 0
    elif p_data6 == '':
        p_data6 = 0

    return p_data1 + p_data2 + p_data3 + p_data4 + p_data5 + p_data6


def process_14(data):
    a = process_13(data)
    b = process_12(data)

    return a /b


def process_15(data):
    return 1 - process_14(data)


def my_sort(data):
    data.sort(
        key=lambda l: (l[2], l[1], l[0])
    )
    return data


def util(data):
    tmp1 = data[0:3]
    tmp2 = process_ed010(data)
    tmp3 = process_ed001(data)
    tmp4 = process_ed023_1(data)
    tmp5 = process_ed024_1(data)
    tmp6 = process_ed023_1_ed024_1(data)
    tmp7 = process_ed002(data)
    tmp8 = process_ee003(data)
    tmp9 = process_ee024_eeo25_ee026(data)
    tmp10 = process_ee027_1(data)
    tmp11 = process_10(data)
    tmp12 = process_11(data)
    tmp13 = process_12(data)
    tmp14 = process_14(data)
    tmp15 = process_15(data)

    tmp1.append(tmp2)
    tmp1.append(tmp3)
    tmp1.append(tmp4)
    tmp1.append(tmp5)
    tmp1.append(tmp6)
    tmp1.append(tmp7)
    tmp1.append(tmp8)
    tmp1.append(tmp9)
    tmp1.append(tmp10)
    tmp1.append(tmp11)
    tmp1.append(tmp12)
    tmp1.append(tmp13)
    tmp1.append(tmp14)
    tmp1.append(tmp15)

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
    row0 = [u'ID', u'householdID', u'communityID', u'fac', u'care', u'Intop', u'Inpay', u'pay/top', u'sick', u'Inpa', u'Inpat', u'Inout', u'pua', u'self', u'b', u'a', u'psu', u'GSP_it']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], common.set_excel_style('Times New Roman', 220, True))
    count = 1
    for row in data:
        for i in range(0, len(row)):
            sheet1.write(count, i, row[i], common.set_excel_style('Times New Roman', 220, True))
        count = count + 1
    work_book.save('/Users/zhangguyuan/Downloads/result/Demographic_Background.xlsx')
