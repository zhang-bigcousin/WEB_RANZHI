# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_Auto
# FileName:      test_page_add_user
# Author:        ZJY
# Datetime:      2022/5/16 15:19
# Description：
# -----------------------------------------------------------------------------------
import time
import unittest
import parameterized

from pages.page_add_user import *
from tool import read_yaml
from tool.get_log import get_log
from tool.read_ini import read_ini


class AddUserCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.au = AddUser('c', r'http://127.0.0.1/')
        cls.au.click('i', 'product-ranzhi')  # 只有首次登录才有这个页面)
        cls.au.login('admin', 123456)
        cls.au.go_to_back_management()

    @classmethod
    def tearDownClass(cls):
        cls.au.quit()

    # 通过excel获取数据二维列表
    # data_adduser = data_page_adduser.data_test_success(r'C:\Users\Administrator\Desktop\python\data1.xlsx','Sheet1')
    # 通过yaml获取数据
    #
    t = time.strftime('%Y_%m_%d_%H_%M_%S')
    data_adduser = read_yaml.get_yaml_data(read_ini('path', 'yaml_path'))
    log = get_log(read_ini('path', 'log_path') + 'ranzhi_adduser{}.log'.format(t))

    @parameterized.parameterized.expand([['qwe5443322', '6554', 123456, 123456, '776543@qq.com', 'yt65', 1]])
    # @unittest.skip('我想跳过它')
    def test_adduser_success(self, account_name, real_name, frist_password, re_password, email, expect_result, order):
        t = time.strftime('%Y_%m_%d_%H_%M_%S')
        actual_result = None
        try:
            # 调用登录页面的方法
            self.au.add_user(account_name, real_name, frist_password, re_password, email)
            self.au.go_to_lastpage(1000)
            # 获取登录后页面的实际文本值，以便进行断言操作
            actual_result = self.au.get_text('cs',
                                             'body > div > div > div > div.col-md-10 > div > div > table > tbody > tr:last-child > td:nth-child(3)')
            # 断言操作，msg这个描述信息只有在断言失败的时候输出
            print(actual_result, expect_result)
            self.assertEqual(expect_result, actual_result, msg='预期结果和实际结果不一致，请排查')
        except:

            # 截图
            self.au.save_screenshot(
                read_ini('path', 'screenshot_path') + 'ranzhi_adduser_success-用例序号{1}{0}.png'.format(t, order))
            # # 日志输出
            # # self.log.error('添加用户的用例数据第{0}条失败了，预期结果:{1},实际结果:{2}不一致,请排查'.format(order,expect_result,actual_result))  # 输出error类型的日志信息
            self.log.error('添加用户的用例数据第{0}条失败了，预期结果:1,实际结果:2不一致,请排查'.format(order))  # 输出error类型的日志信息
            # # self.au.click('cs',
            # #               'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
            raise AssertionError('第{}条测试用例的预期结果和实际结果不一致'.format(order))
        else:
            pass
            self.log.info('添加成功')

        finally:
            pass
            # self.au.click('lt', '签退')
            # orders += 1

    # @parameterized.expand(data_adduser['data_adduser_fail'])
    # @unittest.skip('我想跳过它')
    # def test_adduser_fail(self, username, password, expect_result,order):
    #     try:
    #         # 调用登录页面的方法
    #         self.au.adduser(username, password)
    #         # 获取登录后页面的实际文本值，以便进行断言操作
    #         actual_result = self.au.get_text('cs',
    #                 'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-body > div')
    #         # 断言操作，msg这个描述信息只有在断言失败的时候输出
    #         self.assertEqual(expect_result, actual_result, msg='预期结果和实际结果不一致，请排查')
    #     except:
    #         # 截图
    #         self.au.save_screenshot(read_ini('path', 'screenshot_path') + 'ranzhi_adduser_fail-用例序号{1}{0}.png'.format(t, order))
    #         # 日志输出
    #         self.log.error('登录失败 的用例数据第{}条失败了，请排查'.format(order))  # 输出error类型的日志信息
    #         self.au.click('cs',
    #                       'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
    #         raise AssertionError('第{}条测试用例的预期结果和实际结果不一致'.format(order))
    #
    #     finally:
    #         # orders += 1
    #         self.au.click('cs',
    #                       'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
    #         # self.au.click('lt', '签退')


if __name__ == '__main__':
    unittest.main()
