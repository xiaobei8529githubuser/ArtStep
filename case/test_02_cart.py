"""
购物车测试用例
"""
import unittest

from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.search_list import SearchListProxy
from utils import DriverUtil


class TestCart(unittest.TestCase):
    """购物车测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.search_list_proxy = SearchListProxy()  # 搜索列表业务执行对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 商品详情业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 跳转首页

    def test_cart(self):
        goods_name = '小米手机5'  # 商品名称
        # 搜索商品
        self.index_proxy.search_goods(goods_name)
        # 跳转商品详情页
        self.search_list_proxy.go_to_goods_detail(goods_name)
        # 添加购物车
        self.goods_detail_proxy.add_cart_func()
        # 获取添加结果
        result = self.goods_detail_proxy.get_add_cart_result()
        # 断言判定执行结果
        self.assertIn('添加成功', result)
