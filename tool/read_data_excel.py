# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_ranzhi
# FileName:      page_login_data
# Author:        ZJY
# Datetime:      2022/5/13 16:06
# Description：
# -----------------------------------------------------------------------------------
from openpyxl import *
from parameterized import parameterized

from tool.read_ini import read_ini


def data_test_success(excel_path, excel_sheet):
    # 加载excel和sheet
    wb = load_workbook(excel_path)
    ws = wb[excel_sheet]

    # 读取数据到二维表格
    data_list = []
    for row in ws:
        data_list1 = []
        for col in row:
            data_list1.append(col.value)
        data_list.append(data_list1)
    return data_list[1::]


if __name__ == '__main__':
    print(data_test_success(r'C:\Users\Administrator\Desktop\python\data1.xlsx', 'Sheet1'))

