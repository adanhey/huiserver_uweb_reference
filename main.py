import os
import pytest
from mail_send import *


if __name__ == '__main__':
    pytest.main(['-vs','test_case.py','--clean-alluredir', '--alluredir','./allure-results'])
    os.system("allure generate ./allure-results -o ./reports --clean")
    # pytest.main("-v -s")
    m = SendMail()
    m.send_mail()