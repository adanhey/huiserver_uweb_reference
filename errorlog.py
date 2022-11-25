import logging
import os

logger = logging.getLogger("uweb_reference")  # 设置日志名称
logger.setLevel(logging.DEBUG)  # 设置日志等级
formats = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")  # 设置打印格式
file_url = logging.FileHandler("E:/uweb_reference_check/error.log", mode="a+",
                               encoding="utf8")  # log文件路径
# file_url1 = logging.StreamHandler()  # 操作台打印
file_url.setFormatter(formats)  # 赋予打印格式
# file_url1.setFormatter(formats)

logger.addHandler(file_url)