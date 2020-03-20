"""
订单列表页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderListPage(BasePage):
    """订单列表-对象库层"""

    def __init__(self):
        super().__init__()

        self.wait_for_pay = (By.LINK_TEXT, '待付款')  # 待付款按钮
        self.now_pay = (By.LINK_TEXT, '立即支付')  # 立即支付按钮

    def find_wait_for_pay(self):
        """待付款按钮定位方法"""
        return self.find_element_func(self.wait_for_pay)

    def find_now_pay(self):
        """立即支付按钮定位方法"""
        return self.find_element_func(self.now_pay)


class OrderListHandle(BaseHandle):
    """订单列表-操作层"""

    def __init__(self):
        self.order_list_page = OrderListPage()

    def click_wait_for_pay(self):
        """点击待付款按钮方法"""
        self.order_list_page.find_wait_for_pay().click()

    def click_now_pay(self):
        """点击立即支付按钮方法"""
        self.order_list_page.find_now_pay().click()


class OrderListProxy(object):
    """订单列表-业务层"""

    def __init__(self):
        self.order_list_handle = OrderListHandle()

    def go_to_order_pay(self):
        """跳转订单支付页面方法"""
        self.order_list_handle.click_wait_for_pay()
        self.order_list_handle.click_now_pay()
