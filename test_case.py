from result_check import *

class TestClass:
    @allure.story("更新产品属性")
    def test_product_save(self):
        result = b.product_saveorupdate()
        re_check(result.json(),result.status_code)

    @allure.story("产品新建及删除")
    def test_product_create_then_delete(self):
        b.product_saveorupdate(type="save",productCode='whatever01',productName='whatever01')
        deviceid = b.get_product('whatever01').json()['data']['records'][0]['id']
        result = b.product_delete(deviceid)
        re_check(result.json(),result.status_code)


    @allure.story("新增型号及删除")
    def test_model_create_then_delete(self):
        result = b.model_saveorupdate("whchcaj","whchcaj",type='save')
        modelid = b.get_productmodel("whchcaj").json()['data']['records'][0]['id']
        result_delete = b.model_delete(modelid)
        re_check(result.json(),result.status_code)
        re_check(result_delete.json(),result_delete.status_code)

    @allure.story("批量更新型号")
    def test_model_update_batch(self):
        modelresult = b.get_productmodel(current=5, size=5).json()
        modelidlist = []
        for i in modelresult['data']['records']:
            modelidlist.append(i['id'])
        result = b.model_update_batch(modelidlist)
        re_check(result.json(),result.status_code)

    @allure.story("excel导入型号及删除型号")
    def test_model_import_then_delete(self):
        # excel导入model
        result_import = b.model_import_Excel()
        modelid = b.get_productmodel("uweb_reference").json()['data']['records'][0]['id']
        result = b.model_delete(modelid)
        re_check(result.json(),result.status_code)
        re_check(result_import.json(),result_import.status_code)

    @allure.story("客户创建、更新删除")
    def test_customer_create_update_delete(self):
        result = b.customer_save()
        print(result.text)
        cus_id = b.get_customer(nowtime).json()['data']['records'][0]['id']
        updateresult = b.customer_update(cus_id)
        delete_result = b.customer_delete(cus_id)
        re_check(result.json(),result.status_code)
        re_check(updateresult.json(),updateresult.status_code)
        re_check(delete_result.json(),delete_result.status_code)

    @allure.story("excel导入客户及删除")
    def test_customer_import_and_delete(self):
        result = b.customer_import_excel()
        cus_id = b.get_customer("uweb_reference").json()['data']['records'][0]['id']
        result_delete = b.customer_delete(cus_id)
        re_check(result.json(),result.status_code)
        re_check(result_delete.json(),result_delete.status_code)

    @allure.story("员工新增、更新、删除")
    def test_emp_create_update_delete(self):
        result = b.employee_save()
        empid = b.get_emp().json()['data']['records'][0]['id']
        data = b.get_emp().json()['data']['records'][0]
        result_delete = b.employee_delete(data)
        result_update = b.employee_update(empid)
        re_check(result.json(),result.status_code)
        re_check(result_delete.json(),result_delete.status_code)
        re_check(result_update.json(),result_update.status_code)

    @allure.story("事件查询、确认")
    def test_warn_list_comfirm(self):
        result = b.role_list()
        config_result = b.event_config()
        warn_result = b.warn_batch_status()
        re_check(result.json(),result.status_code)
        re_check(config_result.json(),config_result.status_code)
        re_check(warn_result.json(),warn_result.status_code)
