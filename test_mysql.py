# coding:utf-8

import MySQLdb
import random

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='cz')
# cur = conn.cursor()

#插入
idm = random.randint(1001, 10000)
# idm = 2223
namem = 'cheng'
sexm = 'GG'
phone = random.randint(100000000,199999999)
age = 12
cur = conn.cursor() #游标
sql = 'insert into tb_sm values(%d, "%s", %d, "%s",%d)'%(idm, namem, phone, sexm, age)
cur.execute(sql)  #执行语句
conn.commit()    #提交

#查询
cur.execute("select * from tb_sm")
ret = cur.fetchall()
# print ret
for i in ret:

	print i

cur.close()
conn.close()