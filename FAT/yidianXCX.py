# coding=utf-8
from fastAutoTest.core.wx.wxEngine import WxDriver
import os
import time


def openWechat():
    # 关闭微信
    os.system("adb shell am force-stop com.tencent.mm")
    # 启动微信
    os.system("adb shell am start com.tencent.mm/.ui.LauncherUI")
    time.sleep(5)


# 进入企鹅医典小程序
if __name__ == '__main__':
    # openWechat()
    print "start test..."
    wxDriver = WxDriver()
    wxDriver.wait(1)
    # wxDriver.d(text="发现").click()
    # wxDriver.wait(1)
    # wxDriver.d(text="搜一搜").click()
    # wxDriver.wait(2)
    # wxDriver.d(text="搜索").clear_text()
    # wxDriver.wait(1)
    # wxDriver.d(text="搜索").set_text("腾讯医")
    # wxDriver.wait(5)
    # wxDriver.d(text="腾讯医典").click()
    # wxDriver.wait(1)
    # wxDriver.d(text="小程序").click()
    # wxDriver.wait(1)
    # wxDriver.d(textContains="腾讯医典").click()
    # wxDriver.wait(5)
    wxDriver.initDriver()
    wxDriver.wait(1)

    # time.sleep(3)
    txt = wxDriver.getElementTextByXpath("/html/body/div[1]/div/div[3]/p")
    print txt
    # 点击全部疾病
    wxDriver.clickElementByXpath('/html/body/div[1]/div/div[3]/p')
    # time.sleep(3)
    wxDriver.clickFirstElementByText('白内障')
    # time.sleep(2)
    wxDriver.returnLastPage()
    # time.sleep(2)
    wxDriver.returnLastPage()
    # time.sleep(2)
    # 截图
    # dirPath = os.path.split(os.path.realpath(__file__))[0]
    # PIC_SRC = os.path.join(dirPath, 'pic.png')
    # wxDriver.d.screenshot(PIC_SRC)
    # time.sleep(3)
    wxDriver.close()
