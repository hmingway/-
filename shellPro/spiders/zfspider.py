import scrapy
from shellPro.items import ZfItem
from selenium import webdriver
from redis import Redis


class ZfspiderSpider(scrapy.Spider):
    name = 'zfspider'
    # allowed_domains = ['bj.zu.ke.com']
    start_urls = ['https://wh.zu.ke.com/zufang/pg']
    try:
        conn = Redis('192.168.206.131', port=6379, db=2)
        print('redis连接成功')
    except Exception as e:
        print('连接失败', e)
    t_url = 'https://wh.zu.ke.com/zufang/pg{}/#contentList'
    urls = list(map(lambda i: 'https://wh.zu.ke.com/zufang/pg{}/#contentList'.format(i), [i for i in range(1, 2)]))
    # print(urls)
    house_urls = []

    def parse(self, response):
        house_list = response.xpath('//div[@id="content"]/div[1]/div[1]/div')
        for desc in house_list:
            name = desc.xpath('./a/@title').extract_first()
            url = 'https://wh.zu.ke.com' + desc.xpath('./a/@href').extract_first()
            # print(url)
            conn = self.conn
            reply = conn.sadd('zf_urls', url)
            if reply == 1:
                item = ZfItem()
                item['house_url'] = url
                self.house_urls.append(url)
                # print(item['house_url'])
                # print('有新数据可以爬取')
                yield scrapy.Request(url=url, callback=self.parse_zf_houseInfo, meta={'item': item})
            else:
                print('错误')
                # print('数据暂无更新')

        for pg in range(1, 50):
            url = self.start_urls[0] + str(pg)
            print(url)
            # yield scrapy.Request(url, callback=self.parse)

    def parse_zf_houseInfo(self, response):
        item = response.meat['item']
        print('正在爬取' + item['house_url'])
        item['house_name'] = response.xpath('//div[@class="content clear w1150"]/p/text()').extract_first()
        item['price'] = response.xpath('//div[@id="aside"]/div/span/text()').extract_first()
        item['rent_style'] = response.xpath('//div[@id="aside"]/ul/li[1]/text()').extract_first()
        item['area'] = response.xpath('//div[@id="info"]/ul[1]/li[2]/text()').extract_first()
        item['floor'] = response.xpath('//div[@id="info"]/ul[1]/li[8]/text()').extract_first()
        item['lift'] = response.xpath('//div[@id="info"]/ul[1]/li[9]/text()').extract_first()
        item['park'] = response.xpath('//div[@id="info"]/ul[1]/li[11]/text()').extract_first()
        item['water'] = response.xpath('//div[@id="info"]/ul[1]/li[12]/text()').extract_first()
        item['power'] = response.xpath('//div[@id="info"]/ul[1]/li[14]/text()').extract_first()
        item['gas'] = response.xpath('//div[@id="info"]/ul[1]/li[15]/text()').extract_first()
        item['heating'] = response.xpath('//*[@id="info"]/ul[1]/li[17]/text()').extract_first()
        yield item
