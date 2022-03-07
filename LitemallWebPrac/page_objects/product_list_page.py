# @Author   : Clifford
# @File     : product_list_page
# @Time     : 2022/3/5 14:43
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LitemallWebPrac.page_objects.base_page import BasePage


class ProductListPage(BasePage):

    _TEXT_PRODUCT_NAME = (By.XPATH, "//tbody/tr[1]/td[3]/div")

    # 返回商品的名称
    def get_product_name(self):

        # name = self.driver.find_element(*self._TEXT_PRODUCT_NAME).text
        # print(name)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self._TEXT_PRODUCT_NAME))

        return element.text