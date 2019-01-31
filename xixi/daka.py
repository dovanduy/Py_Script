# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 16:09
# @Author  : chengz
# @File    : daka.py
# @Software: PyCharm
from appium import webdriver
import time


class Daka(object):

    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        # huawei
        desired_caps['deviceName'] = 'b43052845c54'
        # oppo
        # desired_caps['deviceName'] = '93f42dca'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        # desired_caps['resetKeyboard'] = 'True'  # 重置为系统输入法
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def test_bluet(self):
        # 手机有点渣，延时时间搞长点
        time.sleep(10)

        # 点首页的打卡
        self.driver.find_element_by_xpath(
            u"//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()
        time.sleep(5)
        # 进入打卡页面  点击右上角的...
        self.driver.find_element_by_id("com.tencent.wework:id/e3j").click()
        time.sleep(5)

        # 点击进入应用
        self.driver.find_element_by_id("com.tencent.wework:id/nr").click()
        time.sleep(5)

        # 判断有没有打卡
        txt = self.driver.find_element_by_id("com.tencent.wework:id/ahb")

        # 校验下时间，以免重复打
        now_time = int(time.strftime('%H%M'))

        if txt.text == u"上班打卡" and now_time < 901:
            print u"开始上班打卡"
            # txt.click()
            return 1
        elif txt.text == u'下班打卡' and now_time >= 1800:
            print u'开始下班打卡'
            # txt.click()
            return 1
        else:
            print u'已打'

        try:
            # 非常用手机会要确认
            time.sleep(3)
            self.driver.find_element_by_id("com.tencent.wework:id/b4a").click()
        except:
            print "已打卡，无需确认"

        time.sleep(50)


if __name__ == '__main__':

    while True:
        now_time = time.strftime('%H%M')
        # 设置时间，自动执行
        if now_time == '0840':
            print u"准备上班打卡:"
            Daka().test_bluet()
            print u"上班打卡完成"
            break

        elif now_time == "1801":
            print u"准备下班打卡:"
            Daka().test_bluet()
            print u"下班打卡完成"
            break
        else:
            time.sleep(60)
            print u'现在时间=>>>', now_time
