# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:55
# @Author  : chengz
# @File    : se-fat.py
# @Software: PyCharm
import HTMLTestRunner

from fastAutoTest.core.h5.h5Engine import H5Driver
from fastAutoTest.core.wx.wxEngine import WxDriver
import time
import os
import unittest


class SeFAutoTest(unittest.TestCase):
    def setUp(self):
        # 关闭微信
        os.system("adb shell am force-stop com.tencent.mm")
        # 启动微信
        os.system("adb shell am start com.tencent.mm/.ui.LauncherUI")
        time.sleep(5)

    def tearDown(self):
        self.h5Driver.close()

    def test_script(self):
        self.h5Driver = WxDriver()
        self.h5Driver.wait(1)
        self.h5Driver.d(text="发现").click()
        self.h5Driver.wait(1)
        self.h5Driver.d(text="搜一搜").click()
        self.h5Driver.wait(2)
        self.h5Driver.d(text="搜索").clear_text()
        self.h5Driver.wait(1)
        self.h5Driver.d(text="搜索").set_text(u"腾讯医")
        self.h5Driver.wait(10)
        self.h5Driver.initDriver()
        self.h5Driver.wait(3)
        self.h5Driver.d(text="腾讯医典").click()
        self.h5Driver.wait(1)
        # 切换到小程序栏
        self.h5Driver.d(text="小程序").click()
        self.h5Driver.wait(1)
        self.h5Driver.d(textContains="腾讯医典").click()

        self.h5Driver.wait(3)

        self.h5Driver.getMemoryInfo()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SeFAutoTest))
    getTime = time.strftime("%Y%m%d%H%M%S")
    filename = open('%s/test_%s.html' % (os.getcwd(), getTime), 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=filename, verbosity=2, title="xx")

    runner.run(suite)
    filename.close()
