"""
测试套件
"""
import unittest
import config

from case.test_02_cart import TestCart
from case.login import TestLogin
from case.test_03_order import TestOrder
from utils import DriverUtil
from tools.HTMLTestReportCN import HTMLTestRunner

# 初始化套件对象

# suite = unittest.TestSuite()
# 组装测试用例
# suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestCart))
# suite.addTest(unittest.makeSuite(TestOrder))

# 组装用例(第二种方式)
# 注意: 使用加载方式组装测试用例,也有可能出现乱序执行的问题,可以从测试用例文件名上进行排序.
suite = unittest.defaultTestLoader.discover(config.BASE_DIR + '/case/', pattern='test*.py')

# 报告存放的相关设置
report_name = config.BASE_DIR + '/report/report1.html'

# 关闭浏览器退出方法
DriverUtil.change_auto_quit(False)

# 初始化执行对象
# unittest.TextTestRunner().run(suite)
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(f,
                            verbosity=2,
                            title='Web 自动化测试报告',
                            description='测试环境',
                            tester='QA')
    runner.run(suite)

# 打开浏览器退出方法
DriverUtil.change_auto_quit(True)

# 退出浏览器
DriverUtil.quit_driver()
