# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_Auto
# FileName:      get_log
# Author:        ZJY
# Datetime:      2022/5/16 11:26
# Description：
# -----------------------------------------------------------------------------------
import logging


# python里面的logging模块有四大核心类
# Logger 类,日志
# FileHandler 文件处理器
# Filter  过滤器
# Formatter 设置日志格式
def get_log(filename):
    # 实例化对象
    log = logging.Logger('Web_ranzhi')  # 参数name可以理解为一个占位符，可以输入任何值
    # 实例化一个对象，但是这个对象是设置日志输出格式的
    ff = logging.Formatter('[%(filename)s][%(asctime)s][%(levelname)s]:%(message)s')
    # 是将日志输出到指定的位置
    fh = logging.FileHandler(filename, encoding='utf8')
    # 把输出的日志按照设置好的日志格式进行输出
    fh.setFormatter(ff)
    # 把已覆盖好的日志格式添加到log对象里面
    log.addHandler(fh)
    return log
