# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 21:32
# @Author  : chengz
# @File    : XCX.py
# @Software: PyCharm
# 官方地址：https://github.com/Tencent/FAutoTest

from fastAutoTest.core.wx.wxEngine import WxDriver
import os
import time


def openWechat():
    # 关闭微信
    os.system("adb shell am force-stop com.tencent.mm")
    # 启动微信
    os.system("adb shell am start com.tencent.mm/.ui.LauncherUI")
    time.sleep(5)


def xcxOperator():
    print "start test..."
    wxDriver = WxDriver()
    wxDriver.d(text="发现").click()
    wxDriver.wait(1)
    wxDriver.d(text="搜一搜").click()
    wxDriver.wait(1)
    wxDriver.d(text="搜索").clear_text()
    wxDriver.d(text="搜索").set_text("卡亭")
    wxDriver.wait(2)
    wxDriver.d(text="卡亭小程序").click()
    wxDriver.wait(3)
    wxDriver.d(textContains="卡亭小程序 - 小程序").click()



    wxDriver.initDriver()
    txt = wxDriver.getElementTextByXpath("/html/body/div[1]/div/div[3]/p")
    print txt
    # 点击全部疾病
    wxDriver.clickElementByXpath('/html/body/div[1]/div/div[3]/p')
    wxDriver.clickFirstElementByText('白内障')
    wxDriver.returnLastPage()
    wxDriver.returnLastPage()
    # 截图
    # dirPath = os.path.split(os.path.realpath(__file__))[0]
    # PIC_SRC = os.path.join(dirPath, 'pic.png')
    # wxDriver.d.screenshot(PIC_SRC)
    # time.sleep(3)
    wxDriver.close()


# 企鹅医典小程序
if __name__ == '__main__':
    openWechat()
    xcxOperator()
