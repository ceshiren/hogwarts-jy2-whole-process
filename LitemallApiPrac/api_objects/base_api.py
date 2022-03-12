# @Author   : Clifford
# @File     : base_api
# @Time     : 2022/3/12 15:24
import requests

"""
封装底层接口操作
"""

class BaseApi:

    def do_request(self, data: dict):
        if "url" in data:
            return self._http_request(data)
        elif "RPC" in data.get("protocol"):
            self._rpc_request(data)
        elif "TCP" in data.get("protocol"):
            self._tcp_request(data)


    @staticmethod
    def _http_request(data: dict):
        return requests.request(**data)

    @staticmethod
    def _rpc_request(data: dict):
        pass

    @staticmethod
    def _tcp_request(data: dict):
        pass