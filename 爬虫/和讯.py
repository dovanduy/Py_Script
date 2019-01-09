# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 18:07
# @Author  : cz9025
# @PC: chengz


from pyquery import PyQuery
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 "
                  "Safari/537.36",
}
response = requests.get(url="http://money.hexun.com", headers=headers)

div = response.content

print div
