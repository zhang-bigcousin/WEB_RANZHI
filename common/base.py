# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   selenium43
# FileName:      base
# Author:        xm
# Datetime:      2022/5/12 11:26
# Description：
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 变量用名词，方法用动词
# -----------------------------------------------------------------------------------
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self,browser_type,url):
        """

        :param browser_type:浏览器类型(支持首字母大小写,也可使用首字母):Chrome,Firefox,IE
        :param url:需要测试的url地址
        """
        if browser_type in ['Chrome','c','C','chrome']:
                self.driver = webdriver.Chrome()
                # driver = webdriver.Chrome()
        elif browser_type in ['Firefox','f','F','firefox']:
                self.driver = webdriver.Firefox()
        elif browser_type ['ie','IE','i','I']:
                self.driver = webdriver.Ie()
        else:
            raise TypeError('你的浏览器类型输入错误，请排查')
            # print('你的浏览器类型输入错误了')
        # 窗口最大化
        self.driver.maximize_window()
        # 获取测试地址（url）
        self.driver.get(url)


    def element_location(self,method,attribute,group=False):
        """

        :param method: 八大元素定位方法,方法的单词首字母(小写)
        :param attribute: 定位方法对应的属性值
        :param group: 定位的是否是一组元素
        :return:
        """
        dict_method = {'i':By.ID,
                       'cn':By.CLASS_NAME,
                       'tn':By.TAG_NAME,
                       'n':By.NAME,
                       'x':By.XPATH,
                       'plt':By.PARTIAL_LINK_TEXT,
                       'lt':By.LINK_TEXT,
                       'cs':By.CSS_SELECTOR,}
        try:
            ele_method = dict_method[method],attribute
            # print(ele_method)
            # print(*ele_method)
        except:
            raise TypeError ('请输入正确的元素定位方式')
            # print('请输入正确的元素定位方式')
        # if method == 'i' or method == 'id':
        #     ele_method = (By.ID, attribute)
        # elif method == 'n' or method == 'name':
        #     ele_method = By.NAME, attribute
        # elif method == 'cn':
        #     ele_method = By.CLASS_NAME, attribute
        # elif method == 'tn':
        #     ele_method = By.TAG_NAME, attribute
        # elif method == 'lt':
        #     ele_method = By.LINK_TEXT, attribute
        # elif method == 'plt':
        #     ele_method = By.PARTIAL_LINK_TEXT, attribute
        # elif method == 'x':
        #     ele_method = By.XPATH, attribute
        # elif method == 'cs':
        #     ele_method = By.CSS_SELECTOR, attribute
        # else:
        #     raise TypeError('请输入正确的元素定位方式')
        #     # print('请输入正确的定位方式')
        if group == False:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele_method))
            # return self.driver.find_element(*ele_method)
        else:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(ele_method))
            # return self.driver.find_elements(*ele_method)


    def twice_element_location(self, method1, attribute1, method2, attribute2,group=False):
        """

        :param attribute1: 父级定位方法对应的属性值
        :param method1: 父级定位方法,八大元素定位方法,方法的单词首字母(小写),默认By.ID
        :param method2: 子级定位方法,八大元素定位方法,方法的单词首字母(小写),默认By.TAG_NAME
        :param attribute2: 子级定位方法对应的属性值,默认"option"
        :param group:
        :return:
        """
        if method2 == 'i' or method2 == 'id':
            ele_method2 = (By.ID, attribute2)
        elif method2 == 'n' or method2 == 'name':
            ele_method2 = By.NAME, attribute2
        elif method2 == 'cn':
            ele_method2 = By.CLASS_NAME, attribute2
        elif method2 == 'tn':
            ele_method2 = By.TAG_NAME, attribute2
        elif method2 == 'lt':
            ele_method2 = By.LINK_TEXT, attribute2
        elif method2 == 'plt':
            ele_method2 = By.PARTIAL_LINK_TEXT, attribute2
        elif method2 == 'x':
            ele_method2 = By.XPATH, attribute2
        elif method2 == 'cs':
            ele_method2 = By.CSS_SELECTOR, attribute2
        else:
            raise TypeError('请输入正确的元素定位方式')
        if group == False:
            return self.element_location(method1, attribute1).find_element(*ele_method2)
        else:
            return self.element_location(method1, attribute1).find_elements(*ele_method2)


    def send_keys(self, method, attribute, value):
        """

        :param method: 八大元素定位方法,方法的单词首字母(小写)
        :param attribute: 定位方法对应的属性值
        :param value: 需要输入的内容
        :return:
        """
        self.element_location(method,attribute).clear()
        self.element_location(method,attribute).send_keys(value)

    def click(self,method,attribute):
        """

        :param method: 八大元素定位方法,方法的单词首字母(小写)
        :param attribute: 定位方法对应的属性值
        :return:
        """
        self.element_location(method,attribute).click()

    def switch_iframe(self,method):
        """

        :param method: 含name,id,索引
        :return:
        """
        self.driver.switch_to.frame(method)

    def switch_iframe_other(self, method,attribute):
        """

        :param method: 此方法需要元素定位,八大元素定位方法,方法的单词首字母(小写)
        :param attribute: 定位方法对应的属性值
        :return:
        """
        self.driver.switch_to.frame(self.element_location(method,attribute))

    def random_chioce(self, method, attribute):
        """

        :param method: 八大元素定位方法,方法的单词首字母(小写)
        :param attribute: 定位方法对应的属性值
        :return:
        """
        eles = self.element_location(method, attribute,True)
        random.choice(eles).click()

    def random_twice_location(self,method1,attribute1,method2, attribute2):
        """

        :param attribute1: 父级定位方法对应的属性值
        :param method1: 父级定位方法,八大元素定位方法,方法的单词首字母(小写),默认By.ID
        :param method2: 子级定位方法,八大元素定位方法,方法的单词首字母(小写),默认By.TAG_NAME
        :param attribute2: 子级定位方法对应的属性值,默认"option"
        :return:
        """
        sele = self.twice_element_location(method1, attribute1, method2, attribute2,group=True)
        # eles = self.driver.find_element(method1, attribute1).find_elements(method2, attribute2)
        random.choice(sele).click()


    def get_text(self,method,attribute):
        """
        获取元素对应的文本
        :param method:
        :param attribute:
        :return:
        """
        return  self.element_location(method,attribute).text

    def quit(self):
        """
        浏览器的退出操作
        :return: None
        """
        self.driver.quit()


    def save_screenshot(self,filename):
        """
        截图操作
        :param filename: 截图后保存的路径，注意是png格式的文件
        :return:
        """
        self.driver.save_screenshot(filename)



if __name__ == '__main__':

    b = Base('c',r'http://127.0.0.1/ranzhi/sys/user-login.html')
    b.click('i', 'submit')
