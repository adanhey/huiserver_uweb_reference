import os
import pytest
from mail_send import *
from send_report_to_cloud import *


if __name__ == '__main__':
    pytest.main(['-vs','test_case.py','--clean-alluredir', '--alluredir','./allure-results'])
    os.system("allure generate ./allure-results -o ./reports --clean")
    # pytest.main("-v -s")
    upload_result()
    m = SendMail()
    m.send_mail()
