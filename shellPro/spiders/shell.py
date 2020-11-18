import scrapy
from selenium import webdriver
from redis import Redis
from copy import deepcopy
import random
import time
import re
from selenium.webdriver.common.keys import Keys
# from shellPro.items import ShellproItem


# class ShellSpider(scrapy.Spider):
#     name = 'shell'
#     # allowed_domains = ['bj.ke.com', 'sz.ke.com', 'sz.fang.ke.com']
#     start_urls = ['https://bj.ke.com/']
#     models_urls = []
#     models_names = []
#     modelscontent_urls = []
#     # house_info = []
#     # try:
#     #     conn = Redis(('192.168.206.131', 6379), db=2)
#     #     # print('连接成功')
#     # except Exception as e:
#     #     print('连接失败', e)
#
#     def __init__(self):
#         # self.bro = webdriver.Edge(executable_path='../msedgedriver.exe')
#         options = webdriver.ChromeOptions()
#         options.add_argument('--disable-extensions')
#         options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
#         options.add_argument('--start-maximized')
#         self.bro = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/mingyu/PycharmProjects/TestPC/实战项目/chromedriver.exe')
#
#     def parse(self, response):
#         li_list = response.xpath('//*[@class="nav typeUserInfo"]/ul/li')
#         # print(response)
#         model_list = [0, 1, 2]
#         for index in model_list:
#             model_url = li_list[index].xpath('./a/@href').extract_first() + '/'
#             model_name = li_list[index].xpath('./a/text()').extract_first()
#             self.models_names.append(model_name)
#             self.models_urls.append(model_url)
#             # print(model_url, model_name)
#         print(self.models_urls)#######注意没有添加成功, meta={'item': item}
#         for url in self.models_urls:
#             # if url ==
#             yield scrapy.Request(url=url, callback=self.parse_modelsContent)
#
#     def parse_modelsContent(self, response):
#         content_list = response.xpath('//ul[@class="sellListContent"]/li')
#         for desc in content_list:
#             # print('test')
#             urls = desc.xpath('.//div[@class="info clear"]/div[1]/a/@href').extract_first()
#             # print(urls)
#             self.modelscontent_urls.append(urls)
#             # page_num = desc.xpath('./')
#             # img = desc.xpath('./a/img/@src').extract_first()
#             name = desc.xpath('.//div[@class="info clear"]/div[1]/a/text()').extract_first()
#             address = desc.xpath('.//div[@class="info clear"]/div[2]/div[1]/a/text()').extract_first()
#             houserInf = desc.xpath('.//div[@class="info clear"]/div[2]/div[2]//text()').extract()
#             followers = desc.xpath('.//div[@class="info clear"]/div[2]/div[3]//text()').extract()
#             tag = desc.xpath('.//div[@class="info clear"]/div[2]/div[4]//text()').extract()
#             total_price = desc.xpath('.//div[@class="info clear"]/div[2]/div[5]/div[1]//text()').extract()
#             unit_price = desc.xpath('.//div[@class="info clear"]/div[2]/div[5]/div[2]//text()').extract()
#             # item['img'] = img
#             item = ShellproItem()
#             item['name'] = name
#             item['address'] = address
#             item['houseInf'] = houserInf
#             item['followers'] = followers
#             item['tag'] = ' '.join(tag)
#             # item['tag'] = tag
#             item['total_price'] = ''.join(total_price)
#             item['unit_price'] = ''.join(unit_price)
#             item['content_urls'] = self.modelscontent_urls
#             print(item)
#             # yield item
#     #         yield scrapy.Request(url=urls, callback=self.parse_houseInfo, meta={'item': item})
#     #     # print(content_urls)
#     #
#     # def parse_houseInfo(self, response):
#     #
#     #     # print(response)
#     #     item = response.meta['item']
#     #     info = response.xpath('//*[@id="beike"]/div[2]/div[4]/div[1]/div[4]/ul/li')
#     #
#     #     # yield item
#     #     # print(item)
#     def closed(self, spider):
#         self.bro.close()
