# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_ranzhi
# FileName:      page_add_user
# Author:        ZJY
# Datetime:      2022/5/12 20:19
# Description：
# -----------------------------------------------------------------------------------
import time

from pages.page_login import Login


class AddUser(Login):
    # def __init__(self):
    #     pass
    #     # self.driver.get(url)

    def go_to_back_management(self):
        # #点击后台管理
        self.click('x', '/html/body/div[1]/div[1]/div/ul[1]/li[8]/button')
        # 进入iframe框架
        self.switch_iframe(0)
        # 点击添加成员
        self.click('cs', '.user > a')

    def add_user(self, account_name, real_name, frist_password, re_password, email):
        # 填写信息
        self.send_keys('cs', '#account', account_name)
        self.send_keys('cs', '#realname', real_name)
        self.send_keys('cs', '#password1', frist_password)
        self.send_keys('cs', '#password2', re_password)
        self.send_keys('cs', '#email', email)
        self.random_chioce('tn', 'label')
        self.random_twice_location('i', 'dept', 'tn', 'option')
        self.random_twice_location('i', 'role', 'tn', 'option')
        # 提交保存
        self.click('cs', '#submit')

    def go_to_lastpage(self, num_page):
        time.sleep(1)
        self.send_keys('cs', '#_pageID', num_page)
        self.click('cs', '#goto')


if __name__ == '__main__':
    ad = AddUser('C', r'http://127.0.0.1/ranzhi/sys/user-admin.html/')
    # ad.click('i', 'product-ranzhi')
    ad.login('admin', 123456)
    ad.go_to_lastpage(3)
    time.sleep(5)
    ad.quit()
    # ad.go_to_back_management()
    # ad.add_user('汉子','11',123456,123456,"16266@qq.com")
