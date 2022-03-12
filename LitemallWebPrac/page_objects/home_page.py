# @Author   : Clifford
# @File     : home_page
# @Time     : 2022/3/5 14:43
from selenium.webdriver.common.by import By

from LitemallWebPrac.page_objects.base_page import BasePage
import time

class HomePage(BasePage):

    _MENU_PRODUCT_MANAGE = (By.XPATH, "//span[contains(text(), '商品管理')]")
    _MENU_PRODUCT_LAUNCH = (By.XPATH, "//span[contains(text(), '商品上架')]")

    # 点击菜单
    def got_go_product_launch(self):
        time.sleep(2)
        # 点击"商品管理"菜单
        self.do_click(*self._MENU_PRODUCT_MANAGE)

        # 点击"商品上架"菜单
        self.do_click(*self._MENU_PRODUCT_LAUNCH)

        from LitemallWebPrac.page_objects.product_launch_page import ProductLaunchPage
        return ProductLaunchPage(self.driver)
