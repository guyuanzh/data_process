#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd


# 处理Excel数据
def process_excel_r(sheet):
    rows = sheet.nrows
    row_data = []
    for row in range(0, rows):
        row_data.append(sheet.row_values(row))

    id_data_map = {}
    for row in range(1, rows):
        id_data_map[row_data[row][0]] = row_data[row]

    return row_data


# 设置Excel风格
def set_excel_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style


# list转map
def list_data_map(list):

    # data array
    data_map_array = []
    for sheet in list:
        id_list_map = process_excel_r(sheet)
        data_map_array.append(id_list_map)
    return data_map_array


# 返回sheet对象
def read_excel_file(path):
    work_book = xlrd.open_workbook(path)
    sheet = work_book.sheet_by_index(0)
    return sheet
