import datetime
import os
import sys
import allure
import pytest
from errorlog import logger
from interface_document import *


class TestClass:
    @allure.story("添加产品")
    def test_product_save(self):
        result,data,url = b.product_saveorupdate(type="update")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")

    @allure.story("产品更新及删除")
    def test_two(self):
        uwebdeviceid = b.product_saveorupdate(type="save")[0].json()['data']['uwebDeviceId']
        deviceid = b.get_product(nowtime)[0].json()['data']['records'][0]['id']
        result,data,url = b.product_delete(deviceid)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")

    @allure.story("新增型号")
    def test_three(self):
        result,data,url = b.model_saveorupdate()
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")

    @allure.story("更新型号")
    def test_four(self):
        modelresult = b.get_productmodel(current=5, size=5)[0].json()
        modelidlist = []
        for i in modelresult['data']['records']:
            modelidlist.append(i['id'])
        result,data,url = b.model_update_batch(modelidlist)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")

    @allure.story("excel导入型号及删除型号")
    def test_five(self):
        # excel导入model
        b.model_import_Excel()
        modelid = b.get_productmodel("uweb_reference")[0].json()['data']['records'][0]['id']
        result,data,url = b.delete_model(modelid)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")

    @allure.story("客户创建、更新删除")
    def test_six(self):
        result,data,url = b.customer_save()
        cus_id = b.get_customer(nowtime)[0].json()['data']['records'][0]['id']
        updateresult,data2,url2 = b.customer_update(cus_id)
        delete_result,data3,url3 = b.customer_delete(cus_id)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url2}")
        logger.debug(f"请求数据：{data2}")
        logger.debug(f"请求结果：{updateresult.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url3}")
        logger.debug(f"请求数据：{data3}")
        logger.debug(f"请求结果：{delete_result.text}")

    @allure.story("excel导入客户及删除")
    def test_seven(self):
        result,url,data = b.customer_import_excel()
        cus_id = b.get_customer("uweb_reference")[0].json()['data']['records'][0]['id']
        result_delete,url2,data2 = b.customer_delete(cus_id)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url2}")
        logger.debug(f"请求数据：{data2}")
        logger.debug(f"请求结果：{result_delete.text}")

    @allure.story("员工新增、更新、删除")
    def test_eight(self):
        result,url,data = b.employee_save()
        empid = b.get_emp()[0].json()['data']['records'][0]['id']
        data = b.get_emp()[0].json()['data']['records'][0]
        result_delete,url2,data2 = b.employee_delete(data)
        result_update,url3,data3 = b.employee_update(empid)
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url2}")
        logger.debug(f"请求数据：{data2}")
        logger.debug(f"请求结果：{result_delete.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url3}")
        logger.debug(f"请求数据：{data3}")
        logger.debug(f"请求结果：{result_update.text}")

    @allure.story("事件查询、确认")
    def test_nine(self):
        result,url,data = b.role_list()
        config_result,url2,data2 = b.event_config()
        warn_result,url3,data3 = b.warn_batch_status()
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url}")
        logger.debug(f"请求数据：{data}")
        logger.debug(f"请求结果：{result.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url2}")
        logger.debug(f"请求数据：{data2}")
        logger.debug(f"请求结果：{config_result.text}")
        logger.debug(f"日志时间：{datetime.datetime.now()}")
        logger.debug(f"请求url：{url3}")
        logger.debug(f"请求数据：{data3}")
        logger.debug(f"请求结果：{warn_result.text}")
