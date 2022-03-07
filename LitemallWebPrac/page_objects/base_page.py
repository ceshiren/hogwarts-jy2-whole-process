# @Author   : Clifford
# @File     : base_page
# @Time     : 2022/3/5 14:44
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

"""
父类
"""

class BasePage:

    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/"

    def __init__(self, driver:WebDriver = None):

        if driver is None:
            # 初始化浏览器
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.get(self._BASE_URL)

        else:
            self.driver = driver

    def do_click(self, by:By, locator: str):
        self.driver.find_element(by, locator).click()


    def do_send_keys(self, value: str, by: By, locator: str):
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(value)

