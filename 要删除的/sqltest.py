# -*- coding: utf-8 -*-

import MySQLdb

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'czblog',
    'charset': 'utf8'
}

con = MySQLdb.connect(**config)

cur = con.cursor()

# 返回条数
wh = cur.execute("SELECT * FROM user_blogs")
print wh

fet = cur.fetchall()
print fet

title = cur.execute("SELECT title FROM user_blogs where id=%s", '1')

print title

# 获得返回的内容
print cur.fetchall()[0][0].encode('utf-8')

cur.close()
con.close()
