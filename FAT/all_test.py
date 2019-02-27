# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 13:54
# @Author  : chengz
# @File    : all_test.py
# @Software: PyCharm


import HTMLTestRunner
import os,time
import unittest
discover = unittest.defaultTestLoader.discover('sefat')
# print discover

getTime = time.strftime("%Y%m%d%H%M%S")
# print getTime
filename = open('%s/test_%s.html'%(os.getcwd(),getTime),'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=filename,verbosity=2,title="xx")

runner.run(discover)
filename.close()
