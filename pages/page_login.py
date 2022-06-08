# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Web_ranzhi
# FileName:      page_login
# Author:        ZJY
# Datetime:      2022/5/12 19:02
# Description：
# -----------------------------------------------------------------------------------
from common.base import Base


class Login(Base):

    def login(self, username, password):
        # self.click('i','product-ranzhi')  #只有首次登录才有这个页面
        # 登录入口
        self.send_keys('i', 'account', username)
        self.send_keys('i', 'password', password)
        self.click('i', 'submit')
