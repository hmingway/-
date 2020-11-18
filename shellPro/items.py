# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#  模块名称
class ModelItem(scrapy.Item):
    #  模块名称
    model_name = scrapy.Field()
    #  模块的url
    model_url = scrapy.Field()


#  城市名称和城市
class CityItem(scrapy.Item):
    #  城市id
    city_id = scrapy.Field()
    #  城市名称
    city_name = scrapy.Field()


# 二手房
class EsfItem(scrapy.Item):
    #  房价
    total_price = scrapy.Field()
    #  平方价
    price = scrapy.Field()
    #  面积
    area = scrapy.Field()
    #  房户类型
    room_door_type = scrapy.Field()
    #  楼层
    floor = scrapy.Field()
    #  位置
    position = scrapy.Field()
    #  装修
    decoration = scrapy.Field()
    #  电梯
    is_lift = scrapy.Field()
    #  交通出行
    transportation = scrapy.Field()
    #  周边
    ambitus = scrapy.Field()
    #  楼房建筑类型
    building_types = scrapy.Field()
    #  供暖方式
    heating_method = scrapy.Field()
    #  图片
    images = scrapy.Field()


# 新房
class XfItem(scrapy.Item):
    #  房价
    total_price = scrapy.Field()
    #  平方价
    price = scrapy.Field()
    #  地址
    position = scrapy.Field()
    #  物业类型
    wy = scrapy.Field()
    #  楼盘类型
    houses = scrapy.Field()
    #  楼盘地址
    residential_address = scrapy.Field()
    #  售楼地址
    sales_address = scrapy.Field()
    #  开发商
    developers = scrapy.Field()
    #  图片
    images = scrapy.Field()


# 租房
class ZfItem(scrapy.Item):
    #  房子链接
    house_url = scrapy.Field()
    #  房子
    house_name = scrapy.Field()
    #  租房方式
    rent_style = scrapy.Field()
    #  面积
    area = scrapy.Field()
    #  楼层
    floor = scrapy.Field()
    #  电梯
    lift = scrapy.Field()
    #  停车场
    park = scrapy.Field()
    #  供水
    water = scrapy.Field()
    #  电
    power = scrapy.Field()
    #  燃气
    gas = scrapy.Field()
    #  供热
    heating = scrapy.Field()
    #  房价
    price = scrapy.Field()
    #  位置
    position = scrapy.Field()
    #  图片
    images = scrapy.Field()

