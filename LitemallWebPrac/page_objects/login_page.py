# @Author   : Clifford
# @File     : login_page
# @Time     : 2022/3/5 14:43
from selenium.webdriver.common.by import By

from LitemallWebPrac.page_objects.base_page import BasePage


class LoginPage(BasePage):

    _INPUT_USERNAME = (By.XPATH, "//*[@name='username']")
    _INPUT_PASSWORD = (By.XPATH, "//*[@name='password']")
    _BUTTON_LOGIN = (By.CSS_SELECTOR, "button.el-button")

    # 登录
    def login(self):
        # 输入用户名
        self.do_send_keys("admin123", *self._INPUT_USERNAME)
        # 输入密码
        self.do_send_keys("admin123", *self._INPUT_PASSWORD)
        # 点击登录按钮
        self.do_click(*self._BUTTON_LOGIN)

        from LitemallWebPrac.page_objects.home_page import HomePage
        return HomePage(self.driver)
