# coding=utf-8
from fastAutoTest.core.h5.h5Engine import H5Driver
from fastAutoTest.core.wx.wxEngine import WxDriver
import time
import os
from uiautomator import device as dev


# H5 Demo
def openWechat():
    # 关闭微信
    os.system("adb shell am force-stop com.tencent.mm")
    # 启动微信
    os.system("adb shell am start com.tencent.mm/.ui.LauncherUI")
    time.sleep(5)


def testScript():
    print "start test..."
    # device = 'bdefdc13'
    h5Driver = WxDriver()
    h5Driver.wait(1)
    h5Driver.d(text="发现").click()
    h5Driver.wait(1)
    h5Driver.d(text="搜一搜").click()
    h5Driver.wait(2)
    h5Driver.d(text="搜索").clear_text()
    h5Driver.wait(1)
    h5Driver.d(text="搜索").set_text("腾讯医")
    h5Driver.wait(5)
    h5Driver.d(text="腾讯医典").click()
    h5Driver.wait(1)
    h5Driver.d(text="小程序").click()
    h5Driver.wait(1)
    h5Driver.d(textContains="腾讯医典").click()
    # 按键盘的搜索textContains
    # h5Driver.d.click()

    h5Driver.wait(1)


if __name__ == '__main__':
    openWechat()
    testScript()
