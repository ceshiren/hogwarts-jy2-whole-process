# @Author   : Clifford
# @File     : goods_api
# @Time     : 2022/3/12 15:25
import jsonpath

from LitemallApiPrac.api_objects.litemall import Litemall



class GoodsApi(Litemall):

    # 上架商品
    def create(self, goods_sn: str, goods_name: str):

        # logger.info(f"商品编号：{goods_sn}, 商品名称：{goods_name}")

        info = {
            "url": f"{self.base_url}/admin/goods/create",
            "method": "post",
            "headers": {"X-Litemall-Admin-Token": self.token},
            "json": {
                "goods": {
                    "goodsSn": goods_sn,
                    "name": goods_name,
                },
                "specifications": [

                    {

                        "specification": "规格",

                        "value": "标准",

                        "picUrl": ""

                    }

                ],
                "products": [

                    {

                        "id": 0,

                        "specifications": [

                            "标准"

                        ],

                        "price": 0,

                        "number": 0,

                        "url": ""

                    }

                ],
                "attributes": [
                    {"attribute": "材质","value": "纯棉"
                    }]}
        }

        r = self.do_request(info)
        # logger.info(r.json())
        return r

    # 查询商品
    def query(self, goods_name: str = None, goods_sn: str = None, goods_id: str = None):
        info = {
            "url": f"{self.base_url}/admin/goods/list",
            "method": "GET",
            "headers": {"X-Litemall-Admin-Token": self.token},
            "params": {
                "name": goods_name,
                "goodsSn": goods_sn,
                "goodsId": goods_id,
            }
        }

        return self.do_request(info)

    # 删除商品
    def delete(self, goods_id: int):
        info = {
            "url": f"{self.base_url}/admin/goods/delete",
            "method": "post",
            "headers": {"X-Litemall-Admin-Token": self.token},
            "json": {"id": goods_id}
        }

        return self.do_request(info)

    def do_find_id(self, goods_name: str):
        r1 = self.query(goods_name=goods_name)
        result = jsonpath.jsonpath(r1.json(), "$..id")

        if result and len(result) == 1:
            my_id = result[0]
        else:
            return None
        return my_id
