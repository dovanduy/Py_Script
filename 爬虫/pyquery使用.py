# -*- coding: utf-8 -*-

from pyquery import PyQuery

# 可加载一段HTML字符串，或一个HTML文件，或是一个url地址
"""
用法：
    PyQuery("<html><title>hello</title></html>")
    PyQuery(filename=html_file)
    PyQuery(url='http://www.baidu.com')
"""
pq = PyQuery(url='https://news.baidu.com/guonei')

# 获取到的元素不只一个时，html()、text()方法只返回首个元素的相应内容块

# 根据类名、id名得到指定元素
# print pq('ul').filter('.ulist').html()


# 直接根据类名、id名获取元素
# print pq('#col_focus').html()


# attr获取属性值
# print pq('a').eq(0).attr('href')


# 只打印第一个p的
# print pq('p').html()


# find查找元素
# 打印在div中找到的第一个ul
# print pq('div').find('ul').eq(0).html()


# 返回父元素
# print pq('.ulist').parent('div')
# print pq('.ulist').parents('div')


# 子元素
# print pq('.ulist').children()


# 遍历一层后，会返回到上一层，会打印出ul及子元素
# print pq('ul.ulist').find('li').end()


# 清空
# pq('.ulist').find('li').empty()


# 打印所有ulist类下的a标签，下的文本及href值
lista = pq('.ulist a')
print len(lista)
for a in lista.items():
    print a.text(), a.attr('href')
