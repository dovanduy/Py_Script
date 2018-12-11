# coding:utf-8
import unittest
import time
import os
import HTMLTestRunner


def create_suite(ls):
    unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(ls, 'test_*.py')
    for suites in discover:
        for test_case in suites:
            unit.addTest(test_case)

    return unit


ls = 'test-case'

all_suite = create_suite(ls)
datetime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# filename = "E:\\result\\result_baidu_" + datetime + ".html"
filename = "E:\\result\\result_weather.html"
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title=u'XXXX测试报告',
    description=u'用例执行情况'
)

runner.run(all_suite)

fp.close()
