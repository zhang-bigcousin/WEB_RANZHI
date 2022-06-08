import time
import unittest
from parameterized import parameterized

from pages.page_login import Login
from tool.get_log import get_log
from tool import read_yaml
from tool.read_ini import read_ini


class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lo = Login('c', r'http://127.0.0.1/')
        cls.lo.click('i', 'product-ranzhi')  # 只有首次登录才有这个页面)

    @classmethod
    def tearDownClass(cls):
        cls.lo.quit()

    # 通过excel获取数据二维列表
    # data_login = data_page_login.data_test_success(r'C:\Users\Administrator\Desktop\python\data1.xlsx','Sheet1')
    # 通过yaml获取数据

    t = time.strftime('%Y_%m_%d_%H_%M_%S')

    data_login = read_yaml.get_yaml_data(read_ini('path', 'yaml_path'))
    log = get_log(read_ini('path', 'log_path') + 'ranzhi_login{}.log'.format(t))

    # data_login = read_yaml.get_yaml_data(r'C:/Users/Administrator/Desktop/python/Web_ranzhi/data_case/yaml_case.yaml')
    # 通过json获取数据
    # data_login = read_json.get_json_data(
    #     r'C:\Users\Administrator\Desktop\python\Web_ranzhi\data_case\data_case.yml')['data_login_success']
    @parameterized.expand(data_login['data_login_success'])
    # @unittest.skip('我想跳过它')
    def test_login_success(self, username, password, expect_result, order):
        t = time.strftime('%Y_%m_%d_%H_%M_%S')

        try:
            # 调用登录页面的方法
            self.lo.login(username, password)
            # 获取登录后页面的实际文本值，以便进行断言操作
            actual_result = self.lo.get_text('cs', '#mainNavbar > div > ul:nth-child(1) > li > a')
            # self.log.info('已经登录')
            # 断言操作，msg这个描述信息只有在断言失败的时候输出
            self.assertEqual(expect_result, actual_result, msg='预期结果和实际结果不一致，请排查')
        except:
            # 截图
            self.lo.save_screenshot(
                read_ini('path', 'screenshot_path') + 'ranzhi_login_success-用例序号{1}{0}.png'.format(t, order))
            # 日志输出
            self.log.error('登录成功的用例数据第{}条失败了，请排查'.format(order))  # 输出error类型的日志信息
            # self.lo.click('cs',
            #               'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
            raise AssertionError('第{}条测试用例的预期结果和实际结果不一致'.format(order))
        else:
            self.log.info('已经登录')

        finally:
            self.lo.click('lt', '签退')
            # orders += 1

    @parameterized.expand(data_login['data_login_fail'])
    # @unittest.skip('我想跳过它')
    def test_login_fail(self, username, password, expect_result, order):
        try:
            # 调用登录页面的方法
            self.lo.login(username, password)
            # 获取登录后页面的实际文本值，以便进行断言操作
            actual_result = self.lo.get_text('cs',
                                             'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-body > div')
            # 断言操作，msg这个描述信息只有在断言失败的时候输出
            self.assertEqual(expect_result, actual_result, msg='预期结果和实际结果不一致，请排查')
        except:
            # 截图
            self.lo.save_screenshot(
                read_ini('path', 'screenshot_path') + 'ranzhi_login_fail-用例序号{1}{0}.png'.format(t, order))
            # 日志输出
            self.log.error('登录失败 的用例数据第{}条失败了，请排查'.format(order))  # 输出error类型的日志信息
            self.lo.click('cs',
                          'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
            raise AssertionError('第{}条测试用例的预期结果和实际结果不一致'.format(order))

        finally:
            # orders += 1
            self.lo.click('cs',
                          'body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-footer > button')
            # self.lo.click('lt', '签退')


if __name__ == '__main__':
    unittest.main()
