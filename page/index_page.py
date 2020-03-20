"""
首页页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """首页-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类的浏览器对象

        self.login_link = (By.LINK_TEXT, '登录')  # 登录链接
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.search_btn = (By.CLASS_NAME, 'ecsc-search-button')  # 搜索按钮
        self.my_cart_btn = (By.CLASS_NAME, 'share-shopcar-index')  # 我的购物车按钮
        self.my_order_link = (By.LINK_TEXT, '我的订单')  # 我的订单链接

    def find_login_link(self):
        """登录链接的定位方法"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """搜索框的定位方法"""
        return self.find_element_func(self.search_bar)

    def find_search_btn(self):
        """搜索按钮的定位方法"""
        return self.find_element_func(self.search_btn)

    def find_my_cart_btn(self):
        """我的购物车按钮的定位方法"""
        return self.find_element_func(self.my_cart_btn)

    def find_my_order_link(self):
        """我的订单链接的定位方法"""
        return self.find_element_func(self.my_order_link)


class IndexHandle(BaseHandle):
    """首页-操作层"""

    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        """登录链接的点击方法"""
        self.index_page.find_login_link().click()

    def input_search_bar(self, kw):
        """搜索框的输入方法"""
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_search_btn(self):
        """搜索按钮的点击方法"""
        self.index_page.find_search_btn().click()

    def click_my_cart_btn(self):
        """我的购物车按钮点击方法"""
        self.index_page.find_my_cart_btn().click()

    def click_my_order_link(self):
        """我的订单链接点击方法"""
        self.index_page.find_my_order_link().click()


class IndexProxy(object):
    """首页-业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()

    def go_to_login(self):
        """跳转登录页面方法"""
        self.index_handle.click_login_link()

    def search_goods(self, kw):
        """搜索商品方法"""
        # 填写搜索内容
        self.index_handle.input_search_bar(kw)
        # 点击搜索按钮
        self.index_handle.click_search_btn()

    def go_to_my_cart(self):
        """跳转我的购物车页面方法"""
        self.index_handle.click_my_cart_btn()

    def go_to_order_list(self):
        """跳转订单列表页面方法"""
        self.index_handle.click_my_order_link()
