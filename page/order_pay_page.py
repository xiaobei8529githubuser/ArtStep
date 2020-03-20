"""
订单支付页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPayPage(BasePage):
    """订单支付-对象库层"""

    def __init__(self):
        super().__init__()

        self.pay_type = (By.CSS_SELECTOR, '[value="pay_code=cod"]')  # 货到付款
        self.confirm_pay = (By.LINK_TEXT, '确认支付方式')  # 确认支付按钮

    def find_pay_type(self):
        """货到付款定位方法"""
        return self.find_element_func(self.pay_type)

    def find_confirm_pay(self):
        """确认付款定位方法"""
        return self.find_element_func(self.confirm_pay)


class OrderPayHandle(BaseHandle):
    """订单支付-操作层"""

    def __init__(self):
        self.order_pay_page = OrderPayPage()

    def click_pay_type(self):
        """点击货到付款方法"""
        self.order_pay_page.find_pay_type().click()

    def click_confirm_pay(self):
        """点击确认付款方法"""
        self.order_pay_page.find_confirm_pay().click()


class OrderPayProxy(object):
    """订单支付-业务层"""

    def __init__(self):
        self.order_pay_handle = OrderPayHandle()

    def order_pay(self):
        """订单支付方法"""
        self.order_pay_handle.click_pay_type()
        self.order_pay_handle.click_confirm_pay()
