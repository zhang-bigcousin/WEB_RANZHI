# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_ranzhi
# FileName:      read_json
# Author:        ZJY
# Datetime:      2022/5/14 12:39
# Description：
# -----------------------------------------------------------------------------------
import json
import jsonpath

from tool.read_ini import read_ini


def get_json_data(json_file):
    with open(json_file, 'r', encoding="utf-8") as json_data:
        return json.load(json_data)


if __name__ == '__main__':
    get_json_data('../data/data_case.json')
    print(get_json_data('../data/data_case.json')['系统登录']['LoginSuccess'])

    json_file = r"C:\Users\Administrator\Desktop\python\Web_ranzhi\data_case\data_case.json"
    json_data = get_json_data(json_file)
    LoginSuccess = jsonpath.jsonpath(json_data, "$..LoginSuccess")[0]
    print(LoginSuccess)
