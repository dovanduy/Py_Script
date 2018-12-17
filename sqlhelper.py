# coding:utf-8
import MySQLdb
import ConfigParser


class MySQLHelper(object):

    def __init__(self):
        u"""数据库操作类"""
        # 得改成读取配置文件形式
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'czblog',
            'charset': 'utf8'
        }

        self.con = MySQLdb.connect(**config)
        self.cur = self.con.cursor(MySQLdb.cursors.DictCursor)

    def get_one(self, sql, params):
        u"""获得一条数据"""
        self.cur.execute(sql, params)
        data = self.cur.fetchone()
        return data

    def get_many(self, sql, params):
        u"""获得多条数据"""
        self.cur.execute(sql, params)
        data = self.cur.fetchall()
        return data

    def insert_one(self, sql, params):
        u"""插入一条数据"""
        count = self.cur.execute(sql, params)
        if count == 1:
            self.con.commit()
            return u'插入数据成功'
        else:
            return u'插入数据失败'

    def insert_many(self, sql, params):
        u"""插入多条数据"""
        try:
            self.cur.executemany(sql, params)
        except Exception, e:
            return u"批量插入数据失败，错误=>" + str(e)
        else:
            self.con.commit()
            return u'批量插入数据成功'

    def update_one(self, sql, params):
        u"""更新数据"""
        self.cur.execute(sql, params)
        self.con.commit()
        return u'更新数据成功'

    def delete_one(self, sql, params):
        u"""删除一条数据"""
        count = self.cur.execute(sql, params)
        if count == 1:
            self.con.commit()
            return u'删除数据成功'
        else:
            return u'删除数据失败'

    def __enter__(self):
        return self

    def __exit__(self, *exc_type):
        del exc_type
        self.cur.close()
        self.con.close()


if __name__ == '__main__':

    with MySQLHelper() as helper:
        print 'title=>', helper.get_one("SELECT title FROM user_blogs where id=%s", '1')['title'].encode('utf-8')

        print 'id=>', helper.get_many("SELECT id FROM user_blogs where uname_id=%(uname)s", {'uname': 'cz'})

        # 使用字典传递
        # 要用字典的形式？？？？

        # print helper.insert_one("INSERT INTO blog_marks(tags) VALUES(%(tags)s)", {'tags': 'Android'})

        # print helper.insert_one("INSERT INTO blog_marks(tags) VALUES(%s)", ['Android'])

        # print helper.insert_many("INSERT INTO blog_marks(tags) VALUES(%s)", ['aa', 'bb'])

        # print helper.delete_one("DELETE FROM blog_marks WHERE tags = %(tags)s", {'tags': 'Android'})

        # print helper.update_one("UPDATE blog_marks SET tags=%s WHERE tags=%s", ['czcz', 'bb'])
