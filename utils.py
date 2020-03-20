"""
全局工具类
"""
from selenium import webdriver


# 切换到新窗口方法
def switch_to_new_window():
    # 获取浏览器对象
    driver = DriverUtil.get_driver()
    # 获取所有窗口句柄
    handles = driver.window_handles
    # 切换窗口
    # 注意: 通过索引值取出新窗口句柄(索引为-1 永远是新窗口)
    driver.switch_to.window(handles[-1])


# 获取特定文本信息的方法
def get_tips_message(text):
    xpath = '//*[contains(text(),"{}")]'.format(text)
    # 捕获异常 防止定位不到元素,代码中止执行
    try:
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element
    except Exception:
        return False
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

class DriverUtil(object):
    """浏览器驱动类"""

    _driver = None

    _auto_quit = True  # 浏览器退出标记

    @classmethod
    def get_driver(cls):
        """获取浏览器驱动方法"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('')
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器驱动方法"""
        if cls._driver and cls._auto_quit:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def change_auto_quit(cls, auto):
        """修改浏览器退出条件的方法"""
        cls._auto_quit = auto
