"""
全局配置文件
"""
import os
import logging.handlers

# 定义一个常量接收文件的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# print(os.path.dirname(os.path.abspath(__file__)))
# print('>>>>>>')
# print(__file__)

# 日志模块设置方法
def config_log_func():
    # 初始化日志器
    logger = logging.getLogger()

    # 修改默认的日志级别
    # logger.setLevel(level=logging.DEBUG)

    # 初始化处理器
    # 控制台
    sh = logging.StreamHandler()
    # 文件
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/WebAutoTest.log',
                                                   when='s',
                                                   interval=5,
                                                   backupCount=4,
                                                   encoding='utf-8')

    # 初始化格式器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)
    # 格式器添加给处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)
    # 处理器添加给日志器
    logger.addHandler(sh)
    logger.addHandler(th)
