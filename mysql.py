import pymysql
from config import db_info
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


class DB:
    def __init__(self):
        logging.info('连接数据库: {}'.format(db_info.get('database')))
        self.conn = pymysql.connect(
            **db_info,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        logging.info('结束数据库连接: {}'.format(db_info.get('database')))
        self.cursor.close()
        self.conn.close()

    def search(self, sql):
        logging.info('执行sql: {}'.format(sql))
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        return ret


class Count:
    def __init__(self):
        self.db = DB()

    def get_user(self, user_id, password):
        sql = 'select user_id from count where user_id="{0}" and pwd="{1}"'.format(user_id, password)
        ret = self.db.search(sql)
        if ret:
            return ret[0]
        else:
            return None


if __name__ == '__main__':
    Count().get_user('yangkang', '123456')

