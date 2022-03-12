# @Author   : Clifford
# @File     : litemall
# @Time     : 2022/3/12 15:25
from LitemallApiPrac.api_objects.base_api import BaseApi

"""
公共业务封装
"""

class Litemall(BaseApi):

    def __init__(self):
        self.base_url = "http://litemall.hogwarts.ceshiren.com/"
        self.token = self.get_token()


    def get_token(self):
        info = {
            "url": f"{self.base_url}/admin/auth/login",
            "method": "post",
            "json": {"username": "admin123", "password": "admin123"}
        }

        r = self.do_request(info)
        return r.json().get("data").get("token")