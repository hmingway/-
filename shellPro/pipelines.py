# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import pymysql
from redis import Redis


class ShellproPipeline:
    def process_item(self, item, spider):
        if spider.name == 'zfspider':
            conn = spider.conn
            for page_url in spider.urls:
                print(page_url.split('/')[-2][-1])
                try:
                    mapping = {page_url: page_url.split('/')[-2][2:]}
                    conn.zadd('pages_urls', mapping)
                    print(page_url + '页链接插入完毕')
                except Exception as e:
                    print('插入失败', e)
        return item


class PymysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        try:
            self.conn = pymysql.Connect(host='127.0.0.1', port=3306, database='shell', user='root', password='123456', charset='utf8')
            print('mysql数据库连接成功')
        except Exception as e:
            print('连接失败', e)

    def process_item(self, item, spider):
        house_name = item["house_name"]
        area = item["area"]
        price = item["price"]
        floor = item["floor"]
        lift = item["lift"]
        water = item["water"]
        power = item["power"]
        self.cursor = self.conn.cursor()
        # self.conn.open()
        if spider.name == 'zfspider':
            try:
                self.cursor.execute('insert into zfinfo_copy2(house_name, area, price, floor, lift, water, power) values("%s","%s","%s","%s","%s","%s","%s")'%(house_name, area, price, floor, lift, water, power))
                self.conn.commit()
                print(item['house_name'] + '数据插入成功')
            except Exception as e:
                print('插入失败')
                self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()




