"""
订单确认页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderCheckPage(BasePage):
    """订单确认-对象库层"""

    def __init__(self):
        super().__init__()

        self.submit_order_btn = (By.LINK_TEXT, '提交订单')  # 提交订单按钮

    def find_submit_order_btn(self):
        """提交订单按钮的定位方法"""
        return self.find_element_func(self.submit_order_btn)


class OrderCheckHandle(BaseHandle):
    """订单确认-操作层"""

    def __init__(self):
        self.order_check_page = OrderCheckPage()

    def click_submit_order_btn(self):
        """提交订单按钮的点击方法"""
        self.order_check_page.find_submit_order_btn().click()


class OrderCheckProxy(object):
    """订单确认-业务层"""

    def __init__(self):
        self.order_check_handle = OrderCheckHandle()

    def submit_order(self):
        """提交订单方法"""
        self.order_check_handle.click_submit_order_btn()
