# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   excel_word
# FileName:      yaml_class
# Author:        ZJY
# Datetime:      2022/5/7 11:10
# Description：   用于打开yml文件
# -----------------------------------------------------------------------------------
import yaml
from tool.read_ini import read_ini


def get_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8") as yaml_data:
        return yaml.safe_load(yaml_data)


if __name__ == '__main__':
    print(
        get_yaml_data(read_ini('path', 'yaml_path'))
    )
