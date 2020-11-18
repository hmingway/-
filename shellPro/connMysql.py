import pymysql


##  文件名报错
class PymysqlPipeline(object):
    conn = None
    cursor = None

    def open_mysql(self, database):
        try:
            self.conn = pymysql.Connect(host='127.0.0.1', port=3306, database='shell', user='root', password='123456', charset='utf8')
            print('连接成功')
        except Exception as e:
            print('连接失败', e)
        # self.conn.close()

    def insert_val(self, table):
        try:
            self.cursor = self.conn.cursor()
            # self.conn.open()
            sql = 'insert into zfinfo(house_name, area, price, floor, lift, water, power)' \
                  'values("%s","%s","%s","%s","%s","%s","%s")%(item["house_name"], item["area"], item["price"], item["floor"], item["lift"], item["water"], item["power"])'
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                print('插入成功')
            except Exception as e:
                print('插入失败')
                self.conn.rollback()
        except Exception as e:
            print('初始化失败')





if __name__ == '__main__':
    host = '127.0.0.1'
    port = 3306
    database = 'shell'
    mysql = PymysqlPipeline(host, port)
    mysql.open_spider(database)