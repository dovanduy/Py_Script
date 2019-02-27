# coding:utf-8
import unittest
import time
import os
import HTMLTestRunner

ls = 'test-case'

all_suite = unittest.defaultTestLoader.discover(ls, 'test_*.py')
getTime = time.strftime('%Y%m%d%H%M%S')

fp = open("%s/result_%s.html" % (os.getcwd(), getTime), "wb")

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title=u'XXXX测试报告',
    description=u'用例执行情况'
)

runner.run(all_suite)

fp.close()
