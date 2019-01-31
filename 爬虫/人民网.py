# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 18:07
# @Author  : cz9025
# @PC: chengz
from concurrent.futures import ThreadPoolExecutor
from pyquery import PyQuery
import requests, json
import time

# 将verify置为False表示不需要验证SSL证书。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 "
                  "Safari/537.36",
}


def get_pyquery(url):
    response = requests.get(url=url, headers=headers)
    print response.encoding
    response.encoding="gb2312"
    if response.status_code == 200:
        # print requests.utils.get_encodings_from_content(response.text)
        pq = PyQuery(response.text)
        return pq


def hx_money(res):
    pq = res.result()

    headingNews = pq('.headingNews_box .headingNews:first').find(".hdNews")
    for news in headingNews.items():
        a = news.find("strong a")
        a_title = a.text()
        a_href = a.attr("href")
        gray = news.find("p a").text()

        print a_title, a_href

        # print "======================"


with ThreadPoolExecutor(10) as p:
    p.submit(get_pyquery, "http://house.people.com.cn").add_done_callback(hx_money)
