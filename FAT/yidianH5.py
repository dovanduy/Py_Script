# coding=utf-8
from fastAutoTest.core.h5.h5Engine import H5Driver
import time
import os
from uiautomator import  Device

# H5 Demo
def openWechat():
    print "start wechat..."
    # 关闭微信
    os.system("adb shell am force-stop com.tencent.mm")
    # 启动微信
    os.system("adb shell am start com.tencent.mm/.ui.LauncherUI")
    time.sleep(5)
    print "start wechat end..."


def testScript():
    # R9S  device = 'bdefdc13'
    # x9007  device = '93f42dca'
    print "start test..."

    h5Driver = H5Driver()
    h5Driver.wait(1)
    h5Driver.d(text="发现").click()
    h5Driver.wait(1)
    h5Driver.d(text="购物").click()
    h5Driver.wait(5)

    h5Driver.initDriver()
    url = "http://h5.baike.qq.com/mobile/enter.html"
    h5Driver.navigateToPage(url)
    h5Driver.wait(3)

    h5Driver.wait(1)
    pa = h5Driver.getElementByXpath('/html/body/div[1]/div/div[3]/p')
    print 'getElementByXpath', pa
    pa = h5Driver.getElementTextByXpath('//p[@class="disease-all"]')
    print 'getElementTextByXpath', pa
    # 全部疾病
    h5Driver.clickElementByXpath('//p[@class="disease-all"]')
    h5Driver.clickFirstElementByText('白内障')
    print "进入白内障"
    h5Driver.returnLastPage()
    h5Driver.returnLastPage()

    txt = h5Driver.getElementByXpath('//p[@class="disease-all"]')
    print 'getElementByXpath', txt
    txt = h5Driver.getElementTextByXpath('//p[@class="disease-all"]')
    print 'getElementTextByXpath', txt
    currhtml = h5Driver.getCurrentPageUrl()
    print "当前url：", currhtml
    context = h5Driver.getAllContext()
    print 'context', context
    node = h5Driver.getBodyNode()
    print 'node', node
    memory = h5Driver.getMemoryInfo()
    print 'memory', memory
    # cpu = h5Driver.getCPUInfo()
    # print 'cpu', cpu
    document = h5Driver.getDocument()
    print 'document', document
    # 关闭整个H5窗口
    h5Driver.wait(3)
    h5Driver.closeWindow()


if __name__ == '__main__':
    openWechat()
    testScript()
