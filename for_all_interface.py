import datetime
import hashlib
import logging

import requests
import setting

env = setting.nowenv


class Huiserver_interface():
    def __init__(self):
        self.host = env['host']
        self.logininfo = self.get_cookie("sysadmin", "hc300124")
        self.cookie = self.logininfo.cookies
        self.customercode = self.logininfo.json()['company']['customerCode']
        self.companyid = self.logininfo.json()['company']['id']
        self.logger = logging.getLogger("uweb_reference")  # 设置日志名称
        self.logger.setLevel(logging.DEBUG)  # 设置日志等级
        self.formats = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")  # 设置打印格式
        self.file_url = logging.FileHandler("E:/uweb_reference_check/error.log", mode="a+",
                                            encoding="utf8")  # log文件路径
        # file_url1 = logging.StreamHandler()  # 操作台打印
        self.file_url.setFormatter(self.formats)  # 赋予打印格式
        self.logger.addHandler(self.file_url)
        self.allcookie = {
            "serviceperson": self.get_cookie(env['%s_serviceperson' % env['mark']]['userName'],
                                             env['%s_serviceperson' % env['mark']]['password']),
            "serviceeengineer": self.get_cookie(env['%s_serviceeengineer' % env['mark']]['userName'],
                                                env['%s_serviceeengineer' % env['mark']]['password']),
            "elecengineer": self.get_cookie(env['%s_elecengineer' % env['mark']]['userName'],
                                            env['%s_elecengineer' % env['mark']]['password']),
            "admin": self.get_cookie(env['%s_admin' % env['mark']]['userName'],
                                     env['%s_admin' % env['mark']]['password']),
            "costumeradmin": self.get_cookie(env['%s_costumeradmin' % env['mark']]['userName'],
                                             env['%s_costumeradmin' % env['mark']]['password']),
            "costumeremp": self.get_cookie(env['%s_costumeremp' % env['mark']]['userName'],
                                           env['%s_costumeremp' % env['mark']]['password']),
        }

    def get_cookie(self, name, password):
        url = '%s/itas-app/userLogin' % self.host
        md5_pd = hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
        data = {"userName": name, "password": md5_pd}
        login = requests.post(url=url, data=data)
        assert login.status_code == 200
        return login

    def take_cookie(self, user=None):
        if user:
            coo = self.allcookie['%s' % user]
            return coo
        else:
            return self.cookie

    def get_request(self, url, param=None, json=None, data=None, headers=None, user=None):
        cookie = self.take_cookie(user)
        result = requests.Session().get(url=url, params=param, json=json, data=data, headers=headers, cookies=cookie)
        self.logger.debug(f"日志时间：{datetime.datetime.now()}")
        self.logger.debug(f"请求url：{url}")
        self.logger.debug(f"请求数据：{param, json, data}")
        self.logger.debug(f"请求结果：{result.text}")
        return result

    def post_request(self, url, param=None, json=None, data=None, headers=None, user=None, files=None):
        cookie = self.take_cookie(user)
        result = requests.Session().post(url=url, params=param, json=json, data=data, headers=headers, cookies=cookie,
                                         files=files)
        self.logger.debug(f"日志时间：{datetime.datetime.now()}")
        self.logger.debug(f"请求url：{url}")
        self.logger.debug(f"请求数据：{param, json, data}")
        self.logger.debug(f"请求结果：{result.text}")
        return result

    def put_request(self, url, param=None, json=None, data=None, headers=None, user=None):
        cookie = self.take_cookie(user)
        result = requests.Session().put(url=url, params=param, json=json, data=data, headers=headers, cookies=cookie)
        self.logger.debug(f"日志时间：{datetime.datetime.now()}")
        self.logger.debug(f"请求url：{url}")
        self.logger.debug(f"请求数据：{param, json, data}")
        self.logger.debug(f"请求结果：{result.text}")
        return result

    def delete_request(self, url, param=None, json=None, data=None, headers=None, user=None):
        cookie = self.take_cookie(user)
        result = requests.Session().delete(url=url, params=param, json=json, data=data, headers=headers, cookies=cookie)
        self.logger.debug(f"日志时间：{datetime.datetime.now()}")
        self.logger.debug(f"请求url：{url}")
        self.logger.debug(f"请求数据：{param, json, data}")
        self.logger.debug(f"请求结果：{result.text}")
        return result

    def patch_request(self, url, param=None, json=None, data=None, headers=None, user=None):
        cookie = self.take_cookie(user)
        result = requests.Session().patch(url=url, params=param, json=json, data=data, headers=headers, cookies=cookie)
        self.logger.debug(f"日志时间：{datetime.datetime.now()}")
        self.logger.debug(f"请求数据：{param, json, data}")
        self.logger.debug(f"请求结果：{result.text}")
        return result