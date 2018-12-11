# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:29
# @Author  : chengz
# @File    : 连数据库.py
# @Software: PyCharm


import MySQLdb

# 也可以使用字典进行连接参数的管理
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'shoppe',
    'charset': 'utf8'
}
con = MySQLdb.connect(**config)

# con = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shoppe', charset='utf8')

cur = con.cursor()

'''
cur.execute(
    "INSERT INTO shopapp_shopp(name,phone,sex,pwd,email) VALUES ('%s', '%s','%d','%s','%s')" % ('cheng', '132333333', 2, '123789', 'a@v.com'))
    
'''
rows = cur.execute("update shopapp_shopp set pwd='666888' where name = '123'")
# rows = cur.execute("SELECT * FROM shopapp_shopp")

# rows=cur.fetchall()
print rows
con.commit()
cur.close()
