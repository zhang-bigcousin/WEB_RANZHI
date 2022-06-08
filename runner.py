# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_Auto
# FileName:      running
# Author:        ZJY
# Datetime:      2022/5/16 13:55
# Description：
# -----------------------------------------------------------------------------------
import unittest
from HTMLTestRunner import HTMLTestRunner

from test.test_page_login import LoginTestCase
from data_case.read_ini import read_ini
import time

class Runner:
    def runner(self):
        #实例化一个套件（相当于一个篮子，装测试用例的）
        suite = unittest.TestSuite()
        cases = read_ini('path','yaml_path')
        # 批量添加测试用例
        suite.addTests(unittest.TestLoader().discover(cases,pattern='loginpage_test.py'))

        t = time.strftime('%Y_%m_%d_%H_%M_%S')
        #报告生成路径和命名
        report = read_ini('path','report_path')+'ranzhireport{}.html'.format(t)
        #写入数据到报告
        with open(report,mode='w',encoding='utf8') as fp:
            #表头
            h = HTMLTestRunner.HTMLTestRunner(fp,title='ranzhi测试报告',description='下面是ranzhi的测试报告内容')
            #写入运行后的数据
            h.run(suite)



if __name__ == '__main__':
    r = Runner()
    r.runner()

