import jsonpath
from interface_document import *
import allure
from interfaceresult_info import *


def re_check(result, resultcode,interface_uri=None):
    assert resultcode == 200
    if interface_uri:
        for i in result_check:
            if i['uri'] == interface_uri:
                for key, value in i['result_dict'].items():
                    dd = jsonpath.jsonpath(result, '$..%s' % key)
                    if value == "str":
                        pass
                    elif value == "int":
                        pass
                    elif value == "float":
                        pass
                    elif value == 'list':
                        pass
                    else:
                        pass

