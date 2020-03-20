from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.locator.login_locator import LoginLocator


class LoginPage(BasePage):
    """登录-对象库层"""

    def __init__(self):
        super().__init__()

        self.username = (By.XPATH, LoginLocator.username)  # 用户名
        self.password = (By.XPATH, LoginLocator.password)  # 密码
        self.login_btn = (By.NAME, LoginLocator.loginbtn)  # 登录按钮

    def set_user(self,value):
        """用户名输入方法"""
        self.find_element_func(self.username).clear()
        self.find_element_func(self.username).send_keys(value)
    def set_btn(self):
        """用户名输入方法"""
        self.find_element_func(self.login_btn).click()