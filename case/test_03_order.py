"""
提交订单测试用例(不能单独执行, 依赖登录和添加购物车逻辑)
"""
import time
import unittest

from page.index_page import IndexProxy
from page.my_cart_page import MyCartProxy
from page.order_check_page import OrderCheckProxy
from page.order_list_page import OrderListProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil, get_tips_message, switch_to_new_window


class TestOrder(unittest.TestCase):
    """订单测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.my_cart_proxy = MyCartProxy()  # 我的购物车业务执行对象
        cls.order_check_proxy = OrderCheckProxy()  # 订单确认业务执行对象
        cls.order_list_proxy = OrderListProxy()  # 订单列表业务执行对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 跳转首页

    def test01_submit_order(self):
        # 点击购物车
        self.index_proxy.go_to_my_cart()

        # 点击去结算
        self.my_cart_proxy.go_to_order_check()

        time.sleep(3)

        # 提交订单
        self.order_check_proxy.submit_order()

        # 设置断言, 判定执行结果
        result = get_tips_message('订单提交成功，请您尽快付款')
        self.assertTrue(result)

    def test02_order_pay(self):
        # 跳转订单列表
        self.index_proxy.go_to_order_list()

        # # 获取所有窗口句柄
        # handles = self.driver.window_handles
        # # 切换窗口
        # # 注意: 通过索引值取出新窗口句柄(索引为-1 永远是新窗口)
        # self.driver.switch_to.window(handles[-1])

        # 切换新窗口
        switch_to_new_window()

        # 跳转支付页面
        self.order_list_proxy.go_to_order_pay()

        # 切换新窗口
        switch_to_new_window()

        # 支付订单
        self.order_pay_proxy.order_pay()
        # 设置断言,判定指定结果
