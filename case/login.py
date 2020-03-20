"""
登录模块测试用例
"""
import json
import logging
import time
import unittest
# import config
from base import *

from page.index_page import IndexProxy
from page.login_page import LoginProxy, LoginPage
from utils import DriverUtil
from parameterized import parameterized


# 数据源解析方法
# def build_login_data():
#     # with open('./data/login_data.json', encoding='utf-8') as f:
#     with open(config.BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
#         data = json.load(f)
#         # 声明空列表
#         data_list = list()
#         # print(data.values())
#         for i in data.values():
#             data_list.append((i.get('username'),
#                               i.get('password')))
#         print(data_list)
#         return data_list


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        # cls.index_proxy = IndexProxy()  # 首页业务执行对象
        # cls.login_proxy = LoginProxy()  # 登录页业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    # def test_login(self):
    #     # 打开首页,点击登录链接
    #     self.index_proxy.go_to_login()
    #
    #     # 执行登录操作
    #     self.login_proxy.login('13800001111', '123456', '8888')
    #
    #     # 断言判定执行结果
    #     # 获取页面标题
    #     time.sleep(3)
    #     title = self.driver.title
    #     self.assertIn('我的账户', title)

    # @parameterized.expand(build_login_data())
    def test_login(self):
        # 打开首页,点击登录链接
        self.driver.get("https://vip.artstep.cn/#/login")
        # LoginPage.set_user(self,'lu1123')
        # LoginPage.set_user(self,'123456')
        # LoginPage.set_btn(self)
        # 执行登录操作
        self.login_proxy.login('lu1123', '123456')

        # # 添加截图功能
        # try:
        #     # 断言判定执行结果
        #     # 获取页面标题
        #     time.sleep(3)
        #     title = self.driver.title
        #     self.assertIn(expect, title)
        # except AssertionError as e:
        #     # 截图
        #     # self.driver.get_screenshot_as_file(config.BASE_DIR + '/screenshot/bug.png')
        #     now_time = time.strftime('%Y%m%d_%H%M%S')
        #     self.driver.get_screenshot_as_file(config.BASE_DIR + '/screenshot/bug_{}_{}.png'.format(now_time, e))
        #     # 抛出异常
        #     raise e

        # logging.info('username={}, pwd={}, code={}, expect={}, title={}'
        #              .format(username,
        #                      pwd,
        #                      code,
        #                      expect,
        #                      title))


# if __name__ == '__main__':
#     unittest.main()
