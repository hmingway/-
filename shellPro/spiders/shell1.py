import scrapy
from selenium import webdriver
# from shellPro.items import ShellproItem
from copy import deepcopy
import time
from redis import Redis


# class Shell1Spider(scrapy.Spider):
#     name = 'shell1'
#     allowed_domains = ['bj.ke.com']
#     # ssl._create_default_https_context = ssl._create_unverified_context
#     start_urls = ['https://bj.ke.com/']
#     modelscontent_urls = []
#     models = {}
#     models_urls = []
#     # try:
#     #     conn = Redis(('192.168.206.131'), port=6379)
#     #     print('连接成功')
#     # except Exception as e:
#     #     print('连接失败', e)
#
#     def __init__(self):
#
#         options = webdriver.ChromeOptions()
#         options.add_argument('--disable-extensions')
#         options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
#         options.add_argument('--start-maximized')
#         self.bro = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/mingyu/PycharmProjects/TestPC/实战项目/chromedriver.exe')
#
#     #找出模板快对应的url
#     def parse(self, response):
#
#         li_list = response.xpath('//*[@class="nav typeUserInfo"]/ul/li')
#         model_list = [0, 1, 2]
#         ##   找出模块
#         for index in model_list:
#             model_url = li_list[index].xpath('./a/@href').extract_first() + '/'
#             model_name = li_list[index].xpath('./a/text()').extract_first()
#             self.models_urls.append(model_url)
#             self.models[model_name] = model_url
#         print(self.models)
#         for name, url in self.models.items():
#             if name == '二手房':
#                 yield scrapy.Request(url=url, callback=self.parse_esfContent, meta={'name': '二手房'})
#             elif name == '新房':
#                 yield scrapy.Request(url=url, callback=self.parse_lpContent, meta={'item': '新房'})
#             elif name == '租房':
#                 yield scrapy.Request(url=url, callback=self.parse_zfContent, meta={'name': '租房'})
#
#     #找出贝壳网二手房详情页面url
#     def parse_esfContent(self, response):
#         item = ShellproItem()
#         house_names = []
#         house_urls = []
#         ##  传过来的模块名称
#         name = response.meta['name']
#         #   解析出房子信息所在的无序列表
#         esf_content_list = response.xpath('//ul[@class="sellListContent"]/li')
#         print(len(esf_content_list))
#         #  循环取出每个房子的详情页url
#         for desc in esf_content_list:
#             house_name = desc.xpath('./a/img[1]/@title').extract_first()
#             urls = desc.xpath('.//div[@class="info clear"]/div[1]/a/@href').extract_first()
#             if urls and house_name is not None:
#                 self.modelscontent_urls.append(urls)
#                 house_urls.append(urls)
#                 house_names.append(house_name)
#                 item[name] = [{name: url for name in house_names for url in house_urls}]
#                 yield scrapy.Request(url=urls, callback=self.parse_esf_houseInfo, meta={'item': item})
#
#     ##  找出贝壳网新房详情页url
#     def parse_lpContent(self, response):
#         item = response.meta['item']
#         lp_content_list = response.xpath('//div[@class="resblock-list-container clearfix"]/ul[2]/li')
#         for desc in lp_content_list:
#             urls = 'https://sz.fang.ke.com' + desc.xpath('./a/@href').extract_first()
#             yield scrapy.Request(url=urls, callback=self.parse_lp_houseInfo, meta={'item': item})
#
#     #找出贝壳网租房详情页url
#     def parse_zfContent(self, response):
#         print('已经到达该网页')
#         name = response.meta['name']
#         item = ShellproItem()
#         zf_content_list = response.xpath('//div[@class="content__article"]/div[1]').extract_first()
#         print(zf_content_list)
#         for desc in zf_content_list:
#             url = 'https://sz.zu.ke.com' + desc.xpath('./div/a/@href').extract_first()
#             yield scrapy.Request(url=url, callback=self.parse_zf_houseInfo, meta={'item': item})
#
#     ##通过二手房的详情url找出对应房的信息
#     def parse_esf_houseInfo(self, response):
#         item = response.meta['item']
#         total_price = response.xpath('//div[@class="overviewIntro"]/div[1]/div[2]/div[1]/span//text()').extracr()
#         item['total_price'] = total_price
#         yield item
#
#     #通过新房对应的房子的详情信息：
#     def parse_lp_houseInfo(self, response):
#         item = response.meta['item']
#         item['unit_price'] = response.xpath('//div[@class="mod-wrap mod-banner"]/div[2]/div/div[2]/span[2]/text()').extract_first()
#         item['total_price'] = response.xpath('//div[@class="mod-wrap mod-banner"]/div[2]/div/div[2]/span[3]/text()').extract_first() + '万'
#         yield item
#
#
#     #通过租房解析出的url找出对应房子的详细信息：
#     def parse_zf_houseInfo(self, response):
#         item = response.meta['item']
#         item['houseInf_name'] = response.xpath('//div[@class="content clear w1150"]/p/text()').extract_first()
#         item['houseInf_name'] = response.xpath('//div[@class="content clear w1150"]/div[2]/div[2]/div/span/text()').extract_first() + '元/月'
#         yield item
#
#     def closed(self, spider):
#         self.bro.close()

