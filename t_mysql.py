# coding:utf-8

import MySQLdb
import random

conn = MySQLdb.connect(host='192.168.1.215', user='golf', passwd='123456', db='golf')
cur = conn.cursor() #游标

# #插入
# idm = random.randint(1001, 10000)
# # idm = 2223
# namem = 'cheng'
# sexm = 'GG'
# phone = random.randint(100000000,199999999)
# age = 12
# sql = 'insert into tb_sm values(%d, "%s", %d, "%s",%d)'%(idm, namem, phone, sexm, age)
# cur.execute(sql)  #执行语句
# conn.commit()    #提交

#查询
cur.execute("select c_user_name, c_password from t_gf_app_user")
ret = cur.fetchall()
# print ret
for i in ret:

	print i

cur.close()
conn.close()
