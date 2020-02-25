#!/usr/bin/env python
# -*- coding: utf-8 -*-
import common
import health_care_and_insurance

if __name__ == "__main__":

    # 获取sheet对象
    sheet = common.read_excel_file(r'/Users/zhangguyuan/Downloads/work/Health_Care_and_Insurance .xlsx')
    id_data_map = common.process_excel_r(sheet)

    data = health_care_and_insurance.process_excel_data(id_data_map)
    print data
    health_care_and_insurance.my_sort(data)
    health_care_and_insurance.process_excel_w(data)
    # data = health_status_and_functioning.process_excel_data(id_data_map)
    # health_status_and_functioning.process_excel_w(data)

