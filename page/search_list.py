"""
搜索列表页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """搜索列表-对象库层"""

    def __init__(self):
        super().__init__()

        # self.goods = (By.XPATH, '//*[@class="shop_name2"]/a[contains(text(),"小米手机5")]')
        self.goods = (By.XPATH, '//*[@class="shop_name2"]/a[contains(text(),"{}")]')

    def find_goods(self, kw):
        """搜索到的商品定位方法"""
        # 通过拼接方式, 将搜索关键字传递到定位信息当中
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表-操作层"""

    def __init__(self):
        self.search_list_page = SearchListPage()

    def click_goods(self, kw):
        """点击搜索到的商品方法"""
        self.search_list_page.find_goods(kw).click()


class SearchListProxy(object):
    """搜索列表-业务层"""
    def __init__(self):
        self.search_list_handle = SearchListHandle()

    def go_to_goods_detail(self, kw):
        """跳转商品详情页面方法"""
        self.search_list_handle.click_goods(kw)
