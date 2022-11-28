import json

from for_all_interface import *
import time

t = time.gmtime()
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", t)
nowdate = time.strftime("%Y%m%d")
date = time.strftime("%Y-%m-%d")


class Uweb_reference(Huiserver_interface):
    def __init__(self):
        super().__init__()
        self.productType = self.dict_list("productType").json()['data']['records'][0]['id']
        self.productname = self.dict_list("productType").json()['data']['records'][0]['dictKey']
        self.workVoltage = self.dict_list("workVoltage").json()['data']['records'][0]['id']
        self.workVoltagename = self.dict_list("workVoltage").json()['data']['records'][0]['dictKey']

    def dict_list(self, dictCode):
        url = '%s/es/dict/list' % self.host
        data = {
            "dictCode": dictCode,
            "current": 1,
            "size": 100,
            "queryChildren": 'true'
        }
        sss = str(data).replace("'true'", 'true')
        sss = sss.replace("'", '"')
        data = json.loads(sss)
        result = self.post_request(url=url, json=data)
        return result

    def product_saveorupdate(self, type='update', customerName='uweb联通测试', modelName='uweb联通测试', productCode='uweb联通测试',
                             productName='uweb联通测试', picUrl=None):
        modelid = self.get_productmodel(modelName).json()['data']['records'][0]['id']
        modelcode = self.get_productmodel(modelName).json()['data']['records'][0]['modelCode']
        customerid = self.get_customer(customerName).json()['data']['records'][0]['id']
        address = self.get_customer(customerName).json()['data']['records'][0]['address']
        contactName = self.get_customer(customerName).json()['data']['records'][0]['contactName']
        productinfo = self.get_product(modelName).json()
        if type == 'update':
            systemCode = productinfo['data']['records'][0]['systemCode']
            proid = productinfo['data']['records'][0]['id']
            productinfo = self.get_product(productName).json()
            uwebDeviceId = productinfo['data']['records'][0]['uwebDeviceId']
            iotData = productinfo['data']['records'][0]['iotData']
            createTime = productinfo['data']['records'][0]['createTime']
            createUser = productinfo['data']['records'][0]['createUser']
        else:
            systemCode = self.get_code("CP")
            proid, uwebDeviceId, iotData = None, None, None
            createUser, createTime = "sysadmin", nowtime
        url = '%s/es/product/saveOrUpdate' % self.host
        data = {
            "id": proid,
            "companyId": self.companyid,
            "createTime": createTime,
            "createUser": createUser,
            "systemCode": systemCode,
            "productCode": productCode,
            "productName": productName,
            "modelName": modelName,
            "modelCode": modelcode,
            "productModel": modelid,
            "productType": self.productType,
            "productTypeName": self.productname,
            "nickName": contactName,
            "address": address,
            "customerId": customerid,
            "buyTime": date,
            "installTime": date,
            "checkTime": date,
            "defendEndTime": date,
            "uwebDeviceId": uwebDeviceId,
            "picUrl": picUrl,
            "iotData": iotData
        }
        result = self.post_request(url=url, json=data)
        return result

    def product_delete(self, proid):
        url = '%s/es/product/delete/%s' % (self.host, proid)
        result = self.get_request(url=url)
        return result

    def getDeviceStatusForApp(self):
        pass

    def model_saveorupdate(self, modelCode, modelName, createTime=nowtime, updateTime=nowtime, type='update',
                           createUser="sysadmin", updateUser="sysadmin", proid=None, uwebModelId=None,
                           machinePower=110, describe=None, modelPic=None, used=1, uwebSourceName=None, deleted=0):
        # 型号创建或修改，code、proid、uwebmodelid传参时代表修改，不带时代表创建
        url = '%s/es/productModel/saveOrUpdate' % self.host
        if type == 'update':
            productinfo = self.get_productmodel(modelName).json()
            uwebSourceName = productinfo['data']['records'][0]['uwebSourceName']
            uwebModelId = productinfo['data']['records'][0]['uwebModelId']
            code = productinfo['data']['records'][0]['sysNo']
            proid = productinfo['data']['records'][0]['id']
        else:
            code = self.get_code("XH")
        data = {
            "id": proid,
            "createTime": createTime,
            "updateTime": updateTime,
            "createUser": createUser,
            "updateUser": updateUser,
            "customerCode": self.customercode,
            "companyId": self.companyid,
            "sysNo": code,
            "modelName": modelName,
            "modelCode": modelCode,
            "productType": self.productType,
            "productName": self.productname,
            "workVoltage": self.workVoltage,
            "workVoltageName": self.workVoltagename,
            "machinePower": machinePower,
            "modelDesc": describe,
            "modelPic": modelPic,
            "used": used,
            "uwebModelId": uwebModelId,
            "uwebSourceName": uwebSourceName,
            "deleted": deleted,
        }
        result = self.post_request(url=url, json=data)
        return result

    def model_update_batch(self, modellist, machinePower=100, systemField=1):
        # 型号列表页修改,批量修改型号属性
        url = '%s/es/productModel/batchUpdate' % self.host
        data = {
            "productType": self.productType,
            "productTypeName": self.productname,
            "workVoltage": self.workVoltage,
            "workVoltageName": self.workVoltagename,
            "machinePower": machinePower,
            "modelDesc": nowtime,
            "ids": modellist,
            "systemField": systemField
        }
        result = self.post_request(url=url, json=data)
        return result

    def model_import_Excel(self):
        # 型号列表页导入excel
        file = open("model.xlsx", 'rb')
        url = '%s/es/productModel/importExcel' % self.host
        data = {
            "file": file
        }
        result = self.post_request(url=url, files=data)
        return result

    def model_delete(self, modelid):
        url = '%s/es/productModel/delete/%s' % (self.host, modelid)
        result = self.get_request(url=url)
        return result

    def product_import_Excel(self):
        # 产品列表页导入excel
        file = open("excel.xlsx", 'rb')
        url = '%s/es/productModel/importExcel' % self.host
        data = {
            "file": file
        }
        result = self.post_request(url=url, files=data)
        return result

    def get_org(self):
        url = '%s/es/department/getList' % self.host
        result = self.post_request(url=url, json={})
        return result

    def customer_update(self, fullName='uweb联通测试', nickName=None, labelList=None, contactName=None, phone=None,
                        logoUrl=None, remark=None, organization=None, managename=None, empname=None, address=None,
                        country=None, city=None, area=None, province=None):
        # 客户列表编辑
        url = '%s/es/customer/update' % self.host
        customerinfo = self.get_customer(fullName).json()
        customerid = customerinfo['data']['records'][0]['id']
        if nickName == None:
            nickName = customerinfo['data']['records'][0]['nickName']
        if contactName == None:
            contactName = customerinfo['data']['records'][0]['contactName']
        if phone == None:
            phone = customerinfo['data']['records'][0]['phone']
        if logoUrl == None:
            logoUrl = customerinfo['data']['records'][0]['logoUrl']
        if remark == None:
            remark = customerinfo['data']['records'][0]['remark']
        if organization == None:
            organization = customerinfo['data']['records'][0]['organization']
            organizationId = customerinfo['data']['records'][0]['organizationId']
        else:
            organizationId = None
            orginfo = self.get_org().json()
            for i in orginfo['data'][0]['children']:
                if i['deptName'] == organization:
                    organization = i['deptName']
                    organizationId = i['id']
                    break
        if managename == None:
            customerManager = customerinfo['data']['records'][0]['customerManager']
            customerManagerId = customerinfo['data']['records'][0]['customerManagerId']
            customerManagerPhone = customerinfo['data']['records'][0]['customerManagerPhone']
        else:
            maninfo = self.get_emp(managename).json()
            customerManager = maninfo['data']['records'][0]['name']
            customerManagerId = maninfo['data']['records'][0]['id']
            customerManagerPhone = maninfo['data']['records'][0]['phone']
        if empname == None:
            employeeName = customerinfo['data']['records'][0]['customerManager']
            employeeId = customerinfo['data']['records'][0]['customerManagerId']
            employeePhone = customerinfo['data']['records'][0]['customerManagerPhone']
        else:
            empinfo = self.get_emp(managename).json()
            employeeName = empinfo['data']['records'][0]['name']
            employeeId = empinfo['data']['records'][0]['id']
            employeePhone = empinfo['data']['records'][0]['phone']
        if address == None:
            address = customerinfo['data']['records'][0]['address']
        if country == None:
            country = customerinfo['data']['records'][0]['address']
        if city == None:
            city = customerinfo['data']['records'][0]['address']
        if area == None:
            area = customerinfo['data']['records'][0]['address']
        if province == None:
            province = customerinfo['data']['records'][0]['address']
        lbl = []
        if labelList:
            dict_info = self.dict_list("customerLabel").json()
            for i in labelList:
                for j in dict_info['data']['records']:
                    if i == j['dictKey']:
                        labeldict = {
                            "labelName": j['dictKey'],
                            "labelId": j['id']
                        }
                        lbl.append(labeldict)
        data = {
            "id": customerid,
            "companyId": self.companyid,
            "customerCode": self.customercode,
            "fullName": fullName,
            "nickName": nickName,
            "labelList": lbl,
            "contactName": contactName,
            "phone": phone,
            "country": country,
            "province": province,
            "city": city,
            "area": area,
            "address": address,
            "organization": organization,
            "organizationId": organizationId,
            "employeeId": employeeId,
            "employeeName": employeeName,
            "employeePhone": employeePhone,
            "customerManagerId": customerManagerId,
            "customerManager": customerManager,
            "customerManagerPhone": customerManagerPhone,
            "remark": remark,
            "logoUrl": logoUrl,
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_code(self, codetype):
        url = '%s/es/common/getCode/%s' % (self.host, codetype)
        result = self.get_request(url=url)
        return result.json()['data']

    def customer_save(self, fullName, nickName, contactName, organization, labelList=None, address=None, country=None,
                      city=None, area=None, province=None, remark=None, logoUrl=None, employeeName=None,
                      customerManager=None):
        if labelList is None:
            labelList = []
        url = '%s/es/customer/save' % self.host
        phone = str(int(time.time()) * 10)[:11]
        code = self.get_code("KH")
        organizationId = None
        orginfo = self.get_org().json()
        for i in orginfo['data'][0]['children']:
            if i['deptName'] == organization:
                organization = i['deptName']
                organizationId = i['id']
                break
        data = {
            "id": "",
            "companyId": "",
            "customerCode": "",
            "customerNumber": code,
            "fullName": fullName,
            "nickName": nickName,
            "labelList": labelList,
            "contactName": contactName,
            "phone": phone,
            "country": country,
            "province": province,
            "city": city,
            "area": area,
            "address": address,
            "industry": "",
            "organization": organization,
            "organizationId": organizationId,
            "remark": remark,
            "logoUrl": logoUrl
        }
        if customerManager:
            maninfo = self.get_emp(customerManager).json()
            data['customerManager'] = maninfo['data']['records'][0]['name']
            data['customerManagerId'] = maninfo['data']['records'][0]['id']
            data['customerManagerPhone'] = maninfo['data']['records'][0]['phone']
        if employeeName:
            empinfo = self.get_emp(customerManager).json()
            data['employeeName'] = empinfo['data']['records'][0]['name']
            data['employeeId'] = empinfo['data']['records'][0]['id']
            data['employeePhone'] = empinfo['data']['records'][0]['phone']
        result = self.post_request(url=url, json=data)
        return result

    def customer_import_excel(self):
        file = open("customer.xlsx", 'rb')
        url = '%s/es/customer/importExcel' % self.host
        data = {
            "file": file
        }
        result = self.post_request(url=url, files=data)
        return result

    def customer_delete(self, cstid):
        url = '%s/es/customer/delete/%s' % (self.host, cstid)
        result = self.get_request(url=url)
        return result

    def employee_save(self, fullName, userName, password, email="", openService=1, role=None):
        if role is None:
            role = ["测试角色"]
        url = '%s/es/employee/saveUser' % self.host
        phone = str(int(time.time()) * 10)[:11]
        data = {
            "id": "",
            "fullName": fullName,
            "userName": userName,
            "password": password,
            "password1": password,
            "linkPhone": phone,
            "email": email,
            "openService": openService,
            "roleIds": ""
        }
        rolelist = self.role_list().json()
        for i in role:
            for j in rolelist['data']:
                if j['roleName'] == i:
                    data['roleIds'] = '%s,%s' % (data['roleIds'], j['id'])
                    break
        result = self.post_request(url=url, json=data)
        return result

    def delete_user(self,userid):
        url = '%s/uweb-monitor/user/deleteUser?userId=%s'%(self.host,userid)
        result = self.delete_request(url=url)
        return result

    def employee_update(self, empid):
        url = '%s/es/employee/update' % self.host
        data = {
            "id": empid,
            "createTime": "2022-11-17 07:00:59",
            "createUser": "sysadmin",
            "updateUser": "sysadmin",
            "customerCode": "0000102074",
            "companyId": "70048941-e07c-4605-8447-2eea1a800573",
            "name": "uwebreference",
            "userName": "",
            "userId": "",
            "jobNumber": "12002312",
            "birthday": "",
            "sex": 1,
            "phone": "",
            "deptId": "755413422017126400",
            "deptName": "测试环境1",
            "deptIds": "_750492929296211968",
            "used": 1,
            "openService": 1,
            "jobKey": "4",
            "jobName": "普通职员",
            "serverOrderNum": 0,
            "assistOrderNum": 0,
            "email": "",
            "supervisor": 0
        }
        result = self.post_request(url=url, json=data)
        return result

    def employee_delete(self, data):
        url = '%s/es/employee/deleteUser' % self.host
        result = self.post_request(url=url, json=data)
        return result

    def role_list(self):
        url = '%s/es/employee/getRoleListByCompanyId' % self.host
        result = self.get_request(url=url)
        return result

    def event_config(self):
        # iot保养提醒
        url = '%s/es/eventPageConfig/getConfig' % self.host
        result = self.get_request(url=url)
        return result

    def warn_batch_status(self, eventIds, ids, eventType=2, handleStatus=2, handleRemark="123"):
        url = '%s/es/warn/batchUpdateStatus' % self.host
        data = {
            "eventIds": [
                eventIds
            ],
            "ids": [
                ids
            ],
            "eventType": eventType,
            "handleStatus": handleStatus,
            "handleRemark": handleRemark
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_product(self, name, current=1, size=20):
        url = '%s/es/product/getPage' % self.host
        data = {
            "productName": name,
            "current": current,
            "size": size
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_productmodel(self, name=None, current=1, size=10):
        url = '%s/es/productModel/getPage' % self.host
        data = {
            "modelName": name,
            "current": current,
            "size": size
        }
        result = self.post_request(url=url, json=data)
        return result

    def delete_model(self, modelid):
        url = '%s/es/productModel/delete/%s' % (self.host, modelid)
        result = self.get_request(url=url)
        return result

    def get_customer(self, name=None, current=1, size=20, labelIds=None, organizationIds=None, customerManagerId="",
                     employeeId="", contactName="", customerNumber=""):
        if organizationIds is None:
            organizationIds = []
        if labelIds is None:
            labelIds = []
        url = '%s/es/customer/list' % self.host
        data = {
            "customerNumber": customerNumber,
            "fullName": name,
            "contactName": contactName,
            "employeeId": employeeId,
            "customerManagerId": customerManagerId,
            "organizationIds": organizationIds,
            "labelIds": labelIds,
            "current": current,
            "size": size
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_emp(self, name="reference", jobNumber="", jobKey="", current=1, size=20):
        orgid = self.get_org().json()['data'][0]['id']
        url = '%s/es/employee/list' % self.host
        data = {
            "jobNumber": jobNumber,
            "name": name,
            "jobKey": jobKey,
            "deptId": orgid,
            "current": current,
            "size": size
        }
        result = self.post_request(url=url, json=data)
        return result


b = Uweb_reference()
# print(b.dict_list("productType").text)
# print(b.product_saveorupdate(type="update").status_code)
# print(b.product_saveorupdate().text)
# deviceid = b.get_product(nowtime).json()['data']['records'][0]['id']
# print(b.product_delete(deviceid).text)
# print(b.model_saveorupdate("uweb联通测试","uweb联通测试",type='save').text)
# update_batch model
# modelresult = b.get_productmodel(current=5,size=5).json()
# modelidlist = []
# for i in modelresult['data']['records']:
#     modelidlist.append(i['id'])
# print(b.model_update_batch(modelidlist).text)
# excel导入model
# print(b.model_import_Excel().text)
# modelid = b.get_productmodel("uweb_reference").json()['data']['records'][0]['id']
# print(b.delete_model(modelid).text)
# 客户创建、编辑及删除
# print(b.customer_save().text)
# cus_id = b.get_customer(nowtime).json()['data']['records'][0]['id']
# print(b.customer_update(cus_id).text)
# print(b.customer_delete(cus_id).text)
# excel导入
# print(b.customer_import_excel().text)
# cus_id = b.get_customer("uweb_reference").json()['data']['records'][0]['id']
# print(b.customer_delete(cus_id).text)
# 用户
print(b.employee_save("11vv1", "c1ced5", "acd41e1v").text)
# print(b.get_emp().text)
# data = b.get_emp().json()['data']['records'][0]
# print(b.employee_delete(data).text)
# print(b.employee_update(empid).text)
