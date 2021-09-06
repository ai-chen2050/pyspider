# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenseaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    themeDomain = scrapy.Field()           # NFT 属于的主题领域
    ntfUrl = scrapy.Field()                # NFT 的公网 URL 挂售地址
    dealPrice = scrapy.Field()             # 最新的成交价格
    onSalePrice = scrapy.Field()           # 当前挂售价格
    rareness = scrapy.Field()              # 稀缺性因子
