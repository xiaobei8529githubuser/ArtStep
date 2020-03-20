"""
商品详情页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super().__init__()

        self.join_cart_btn = (By.ID, 'join_cart')  # 添加购物车按钮
        # self.join_cart_result = (By.CSS_SELECTOR, '[class="conect-title"]')  # 添加购物车的结果
        self.join_cart_result = (By.CSS_SELECTOR, '.conect-title>span')  # 添加购物车的结果

    def find_join_cart_btn(self):
        """加入购物按钮的定位方法"""
        return self.find_element_func(self.join_cart_btn)

    def find_join_cart_result(self):
        """加入购物车结果的定位方法"""
        return self.find_element_func(self.join_cart_result)


class GoodsDetailHandle(BaseHandle):
    """商品详情-操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_join_cart_btn(self):
        """点击添加购物车按钮的方法"""
        self.goods_detail_page.find_join_cart_btn().click()

    def get_join_cart_result(self):
        """获取添加购物车结果的方法"""

        # 切换 frame
        driver = DriverUtil.get_driver()
        # 注意: 除了可以使用能够代表唯一性的某一个属性的属性值及索引值以外,
        # 还可以直接获取 iframe 元素对象,完成 frame 的切换!
        driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

        return self.goods_detail_page.find_join_cart_result().text


class GoodsDetailProxy(object):
    """商品详情-业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    def add_cart_func(self):
        """添加购物车方法"""
        self.goods_detail_handle.click_join_cart_btn()

    def get_add_cart_result(self):
        """获取添加购物车结果的方法"""
        return self.goods_detail_handle.get_join_cart_result()
