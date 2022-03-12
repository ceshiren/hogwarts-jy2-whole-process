# @Author   : Clifford
# @File     : test_goods_api
# @Time     : 2022/3/12 15:25
import json

import allure
import jsonpath as jsonpath

from LitemallApiPrac.api_objects.goods_api import GoodsApi


class TestGoodsApi:

    def setup_class(self):
        self.goods = GoodsApi()
        # 判断是否存在create的数据，如果存在，清理
        create_data_id = self.goods.do_find_id(goods_name="上架专用")
        if create_data_id:
            self.goods.delete(create_data_id)

        # 创造query所用数据
        self.goods.create(goods_sn="111111", goods_name="查询专用")
        # 创造delete所用数据
        self.goods.create(goods_sn="222222", goods_name="删除专用")

    def teardown_class(self):
        # 数据清理
        query_data_id = self.goods.do_find_id("查询专用")
        if query_data_id:
            self.goods.delete(query_data_id)

        create_data_id = self.goods.do_find_id("上架专用")
        if create_data_id:
            self.goods.delete(create_data_id)

    @allure.story("上架测试用例")
    def test_create(self):
        r = self.goods.create(goods_sn="111111", goods_name="上架专用")
        assert r.status_code == 200
        assert r.json().get("errno") == 0
        assert r.json().get("errmsg") == "成功"

        r2 = self.goods.query(goods_name="上架专用")
        result = jsonpath.jsonpath(r2.json(), "$..name")
        assert "上架专用" in result

    @allure.story("查询测试用例")
    def test_query(self):
        r = self.goods.query(goods_name="查询专用")
        print(r.json())
        assert r.status_code == 200
        assert r.json().get("errno") == 0
        assert r.json().get("errmsg") == "成功"

        result = jsonpath.jsonpath(r.json(), "$.data.list")
        assert result
        result2 = jsonpath.jsonpath(r.json(), "$..name")
        assert "查询专用" in result2

    @allure.story("删除测试用例")
    def test_delete(self):

        with allure.step("找到商品id"):
            # 通过商品名称，找到商品id
            my_delete_id = self.goods.do_find_id("删除专用")

        with allure.step("调用删除接口"):
            r2 = self.goods.delete(goods_id=my_delete_id)
        assert r2.status_code == 200
        assert r2.json().get("errno") == 0
        assert r2.json().get("errmsg") == "成功"
