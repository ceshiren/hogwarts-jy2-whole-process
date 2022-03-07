# @Author   : Clifford
# @File     : product_launch_page
# @Time     : 2022/3/5 14:43
from selenium.webdriver.common.by import By

from LitemallWebPrac.page_objects.base_page import BasePage


class ProductLaunchPage(BasePage):

    _INPUT_PRODUCT_CODE = (By.XPATH, "//label[@for='goodsSn']/../div/div/input")
    _INPUT_PRODUCT_NAME = (By.XPATH, "//label[@for='name']/../div/div/input")
    _INPUT_PRODUCT_PRICE = (By.XPATH, "//label[@for='counterPrice']/../div/div/input")
    _RADIO_HOT = (By.XPATH, "//span[contains(text(), '热卖')]")
    _BUTTON_LAUNCH = (By.XPATH, "//div[@class='op-container']//span[contains(text(), '上架')]")

    # 商品上架
    def product_launch(self):

        # 输入"商品编号"
        self.do_send_keys("123124215", *self._INPUT_PRODUCT_CODE)
        # 输入"商品名称"
        self.do_send_keys("Hogwarts", *self._INPUT_PRODUCT_NAME)
        # 输入"市场售价"
        self.do_send_keys("666", *self._INPUT_PRODUCT_PRICE)
        # 点击"热卖"按钮
        self.do_click(*self._RADIO_HOT)

        # 滑动到页面底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 点击"上架"按钮
        self.do_click(*self._BUTTON_LAUNCH)

        from LitemallWebPrac.page_objects.product_list_page import ProductListPage
        return ProductListPage(self.driver)
