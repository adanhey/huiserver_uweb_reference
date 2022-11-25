import os
import pytest



if __name__ == '__main__':
    pytest.main(['-vs','test_case.py','--clean-alluredir', '--alluredir','./allure-results'])
    os.system("allure generate ./allure-results -o ./reports --clean")
    # pytest.main("-v -s")
