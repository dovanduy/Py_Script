# coding:utf-8
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import requests
import time

# p = ThreadPoolExecutor(30)  # 创建1个程池中，容纳线程个数为30个；
title = []


def get_index(url):
    u"""通用请求"""
    respose = requests.get(url)
    if respose.status_code == 200:
        print u"编码方式==>>>", respose.encoding
        return respose.text


def sina_news(res):
    u"""新浪"""
    res = res.result()  # 进程执行完毕后，得到1个对象
    html = etree.HTML(res)
    # 最新新闻
    result = html.xpath('//div[@class="zgjq"]//ul//a')
    print len(result)
    for li in result:
        titlt = li.xpath('./text()')
        if len(titlt):
            print titlt[0].encode('ISO-8859-1'),
            print li.xpath('./@href')


def paper_news(res):
    u"""澎湃"""
    res = res.result()
    html = etree.HTML(res)
    uri = 'https://www.thepaper.cn/'
    a_tesult = html.xpath('//h2/a')
    for a in a_tesult:
        a_img = a.xpath('./../../div[1]/a/img/@src')
        atext = a.xpath('./text()')
        ahref = a.xpath('./@href')
        print atext[0], uri + ahref[0], a_img


def baidu_news(res):
    u"""百度"""
    res = res.result()
    html = etree.HTML(res)
    result = html.xpath('//ul[contains(@class,"ulist")]//a')
    print len(result)
    # global title
    for li in result:
        title.append(li.xpath('./text()')[0])
        print li.xpath('./text()')[0],
        print li.xpath('./@href')


def car_news(res):
    u"""环球汽车"""
    res = res.result()
    html = etree.HTML(res)

    result = html.xpath('//ul[@class="iconBoxT14"]//a')
    print u"环球汽车=>>>",len(result)
    for li in result:
        print li.xpath('./text()')[0].encode('ISO-8859-1'),
        print li.xpath('./@href')


def main():
    with ThreadPoolExecutor(max_workers=10) as p:
        # 新浪军情
        p.submit(get_index, 'https://mil.news.sina.com.cn/').add_done_callback(sina_news)
        # 国内新闻
        p.submit(get_index, 'https://news.baidu.com/guonei').add_done_callback(baidu_news)
        # 环球汽车
        p.submit(get_index, 'http://auto.huanqiu.com/').add_done_callback(car_news)
        list_time = str(time.time()).split('.')
        if int(list_time[1]) < 100:
            list_time[1] = '100'
        last_time = list_time[0] + list_time[1]
        # 时事
        p.submit(get_index, 'https://www.thepaper.cn/load_index.jsp?&pageidx=2&lastTime=' + last_time).add_done_callback(
            paper_news)


if __name__ == '__main__':
    print 'Start...'
    main()
    print 'End...'
