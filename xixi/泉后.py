# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 19:05
# @Author  : cz9025
# @PC: chengz


# 登录、新增员工、客户、订单
# 调用类
from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()
# 进入ERP系统登录页
driver.get("http://t.oa.quanhoo.com")
# 放大浏览器
driver.maximize_window()
# 智能等待时间
driver.implicitly_wait(30)
# 输入账号
driver.find_element_by_name("logincode").send_keys("17600000000")
# 输入密码
driver.find_element_by_name("pwd").send_keys("123456")
# 点击登录
driver.find_element_by_css_selector("[class='el-button el-button--primary']").click()
time.sleep(2)
# 点击CRM
driver.find_element_by_xpath("//span[text()='CRM']").click()
time.sleep(2)
# 点击后台管理
driver.find_element_by_xpath(u"//span[text()='后台管理']").click()
time.sleep(2)
# 点击部门与员工
driver.find_element_by_xpath(u"//span[text()='部门与员工']").click()
time.sleep(2)
# 点击新增员工
driver.find_element_by_xpath("//div[@class='el-form-item__content']/button[2]/span").click()
time.sleep(2)
#
# 一组信息框
inputs = driver.find_elements_by_xpath("//input[@class='el-input__inner']")
# 姓名
inputs[0].send_keys("xixi666")
inputs[1].send_keys("xixi6")
inputs[2].send_keys("17666666666")
inputs[3].send_keys("xixi123")
# 性别
driver.find_element_by_xpath("//div[@class='el-form-item__content']/label[@role='radio'][2]/span[1]").click()
# 部门 //span[text()='泉后集团']
driver.find_element_by_xpath(u"//button/span[text()='选择部门']").click()
driver.find_element_by_xpath(u"//span[text()='泉后集团']").click()
# driver.find_element_by_xpath(u"//span[text()='战略发展部']").click()

# 职位
inputs[4].send_keys(u"测试")
# 职务
inputs[5].click()
# 角色名称
inputs[6].click()

# 保存
driver.find_element_by_xpath("//button/span[text()='保存']").click()
