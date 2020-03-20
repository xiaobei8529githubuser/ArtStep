"""
我的购物车页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyCartPage(BasePage):
    """我的购物车-对象库层"""

    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, 'checkCartAll')  # 全选框
        self.go_pay_btn = (By.LINK_TEXT, '去结算')  # 去结算按钮

    def find_check_all(self):
        """全选框定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_pay_btn(self):
        """去结算按钮的定位方法"""
        return self.find_element_func(self.go_pay_btn)


class MyCartHandle(BaseHandle):
    """我的购物车-操作层"""

    def __init__(self):
        self.my_cart_page = MyCartPage()

    def click_check_all(self):
        """全选框的点击方法"""
        sel_element = self.my_cart_page.find_check_all()
        # 判断全选框状态,非选中再做点击
        if not sel_element.is_selected():
            sel_element.click()

    def click_go_pay_btn(self):
        """去结算按钮的点击方法"""
        self.my_cart_page.find_go_pay_btn().click()


class MyCartProxy(object):
    """我的购物车-业务层"""

    def __init__(self):
        self.my_cart_handle = MyCartHandle()

    def go_to_order_check(self):
        """跳转订单确认页的方法"""
        # 全选购物车商品
        self.my_cart_handle.click_check_all()
        # 去结算
        self.my_cart_handle.click_go_pay_btn()
