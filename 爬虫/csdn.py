# coding:utf-8
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import requests

# 这个最好加入线程，以分类进行爬取
all_title = []


def get_index(url, name):
    # print name
    d = {}
    response = requests.get(url)
    if response.status_code == 200:
        # print response.encoding
        d['name'] = name
        d['text'] = response.text
        return d


def get_py(res):
    # print 'name=>>>>',res
    res = res.result()
    # print res
    html = etree.HTML(res['text'])
    # 不包含特定元素的，这里排除为隐藏的元素
    result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    for li in result:
        mycsdn = {}
        title = li.xpath('./text()')
        if len(title):
            mycsdn[res['name']] = title[1].strip()
            mycsdn['urls'] = li.xpath('./@href')[0]
            all_title.append(mycsdn)


def get_info(res):
    res = res.result()
    print res
    # print res['text']
    html = etree.HTML(res['text'])
    # 不包含特定元素的，这里排除为隐藏的元素；div的列表
    article = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    content = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/p/a')
    for i in range(len(article)):
        mycsdn = {}
        mycsdn[res['name']] = article[i].xpath('./text()')[1].strip()
        mycsdn['urls'] = article[i].xpath('./@href')[0]
        mycsdn['cont'] = content[i].xpath('./text()')[0].strip()
        all_title.append(mycsdn)
    # print all_title


def get_rfs(res):
    res = res.result()
    html = etree.HTML(res)
    # 不包含特定元素的，这里排除为隐藏的元素
    result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    for li in result:
        mycsdn = {}
        title = li.xpath('./text()')
        if len(title):
            mycsdn['tt'] = title[1].strip()
            mycsdn['urls'] = li.xpath('./@href')[0]
            all_title.append(mycsdn)


def get_jmeter(res):
    res = res.result()
    html = etree.HTML(res)
    # 不包含特定元素的，这里排除为隐藏的元素
    result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    for li in result:
        mycsdn = {}
        title = li.xpath('./text()')
        if len(title):
            mycsdn['tt'] = title[1].strip()
            mycsdn['urls'] = li.xpath('./@href')[0]
            all_title.append(mycsdn)


def get_function(res):
    res = res.result()
    html = etree.HTML(res)
    # 不包含特定元素的，这里排除为隐藏的元素
    result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    for li in result:
        mycsdn = {}
        title = li.xpath('./text()')
        if len(title):
            mycsdn['tt'] = title[1].strip()
            mycsdn['urls'] = li.xpath('./@href')[0]
            all_title.append(mycsdn)


def get_interface(res):
    res = res.result()
    html = etree.HTML(res)
    # 不包含特定元素的，这里排除为隐藏的元素
    result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
    for li in result:
        mycsdn = {}
        title = li.xpath('./text()')
        if len(title):
            mycsdn['tt'] = title[1].strip()
            mycsdn['urls'] = li.xpath('./@href')[0]
            all_title.append(mycsdn)


def main():
    with ThreadPoolExecutor(10) as p:
        uri = "https://blog.csdn.net/cz9025/article/category/"
        # python
        p.submit(get_index, uri + '6810218', 'python').add_done_callback(get_info)
        # RF+SE
        # p.submit(get_index, uri + '6810219', 'rfs').add_done_callback(get_py)
        # # JMETER
        # p.submit(get_index, uri + '6858016', 'jmeter').add_done_callback(get_py)
        # # 接口测试
        # p.submit(get_index, uri + '6966010', 'interface').add_done_callback(get_py)
        # # 功能测试
        # p.submit(get_index, uri + '6560600', 'functions').add_done_callback(get_py)


if __name__ == '__main__':
    main()
    # print all_title
    for blog in all_title:
        for k in blog:
            # print
            if k == 'python':
                pass
                # print blog[k], blog['urls']
            # elif k == 'rfs':
            #     print blog[k], blog['urls']
            # elif k == 'jmeter':
            #     print blog[k], blog['urls']
            # elif k == 'interface':
            #     print blog[k], blog['urls']
            # elif k == 'functions':
            #     print blog[k], blog['urls']
