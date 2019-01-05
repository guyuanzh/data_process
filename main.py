#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter

import common
import demographic_background


if __name__ == "__main__":

    # 获取sheet对象
    sheet = common.read_excel_file(r'/Users/zhangguyuan/Downloads/work/Demographic_Background.xlsx')
    id_data_map = common.process_excel_r(sheet)

    data = demographic_background.process_excel_data(id_data_map)
    demographic_background.process_excel_w(data)
    # data = health_status_and_functioning.process_excel_data(id_data_map)
    # health_status_and_functioning.process_excel_w(data)

