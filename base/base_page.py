"""
PO 文件的基类
"""
from utils import DriverUtil


class BasePage(object):
    """对象库层的基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element_func(self, location):
        """元素定位方法"""
        # return self.driver.find_element(location[0], location[1])
        # *location 元组数据拆包操作
        return self.driver.find_element(*location)


class BaseHandle(object):
    """操作层的基类"""

    def input_text(self, element, text):
        element.clear()  # 清空内容
        element.send_keys(text)  # 输入内容
