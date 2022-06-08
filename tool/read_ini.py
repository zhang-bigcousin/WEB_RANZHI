# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_Auto
# FileName:      read_ini
# Author:        ZJY
# Datetime:      2022/5/16 8:54
# Description：
# -----------------------------------------------------------------------------------
import configparser
import os


def read_ini(section, option):
    # 实例化对象
    config = configparser.ConfigParser()
    # 自动获取项目所在路径
    # path = os.getcwd()  #谁调用就返回谁的所在路径
    before_path = os.path.dirname(__file__).split('tool')[0]  # 看__file__文件在哪里
    # print(before_path)
    # 找到ini文件
    config.read(before_path + r'data\path.ini')
    # 获取path下面的路径,section表示读取文件那一部分内容,option表示section中具体的数据,相当于访问多维列表
    after_path = config.get(section, option)
    # 项目路径和数据配置文件中路径进行拼接
    all_path = os.path.join(before_path, after_path)
    return all_path


if __name__ == '__main__':
    print(read_ini('path', 'yaml_path'))
