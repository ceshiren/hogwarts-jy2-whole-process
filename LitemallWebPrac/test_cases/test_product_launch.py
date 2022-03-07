# @Author   : Clifford
# @File     : test_product_launch
# @Time     : 2022/3/5 15:06
from LitemallWebPrac.page_objects.login_page import LoginPage


class TestProductLaunch:



    def test_product_launch(self):

        name = LoginPage()\
            .login()\
            .got_go_product_launch()\
            .product_launch()\
            .get_product_name()

        assert name == "Hogwarts"