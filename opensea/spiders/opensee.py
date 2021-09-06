# -*- encoding: utf-8 -*-
'''
@File    :   opensea.py
@Time    :   2021/08/30 15:33:47
@Author  :   Blake chen
@Contact :   blake.chen@dfgroup.pro
@License :   (C)Copyright 2021, DFG
@Desc    :   Opensea crawler
'''

# here put the import lib

import scrapy, math, time
from urllib import parse
from opensea.items import OpenseaItem
from opensea.settings import selfConfig
from aroay_cloudscraper import CloudScraperRequest
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class OpenseeSpider(scrapy.Spider):
    name = 'opensee'
    allowed_domains = ['opensea.io']
    httpsStr = "https://"
    # start_urls = ['http://opensea.io/']  https://opensea.io/assets?search[query]=cryptopunks
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        self.baseUrl = "https://opensea.io/assets?search[query]="

    def __del__(self):
        self.driver.close()

    def start_requests(self):
        """
        Framwork Callback funtion for replace the start_urls list
        """
        for theme_item in selfConfig.SEARCH_THEME_WORDS:
            yield CloudScraperRequest(self.baseUrl + theme_item, self.parseItemUrl, cb_kwargs={"theme": theme_item}, errback=self.errback_httpbin)

    def parseItemUrl(self, response, theme):
        url_set = set() 
        self.driver.get(response.url)
    
        for i in range(selfConfig.ITERATOR_ROUND_NUM):
            url_set |= set(response.xpath('/html/body/div/div[1]/div/div/main/div/div/div[2]/div[2]/div/div/div/article/a/@href').extract())
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            time.sleep(3)
            response = scrapy.http.HtmlResponse(url = response.url, body = self.driver.page_source.encode('utf-8'), encoding = 'utf-8', status = 200)

        for item in url_set:
            reqUrl = self.httpsStr + self.allowed_domains[0] + item 
            yield CloudScraperRequest(reqUrl, self.parseNftPage, cb_kwargs={"theme": theme} ,errback=self.errback_httpbin)
            
    def parseNftPage(self, response, theme):
        item = OpenseaItem()
        item['ntfUrl'] = parse.unquote(response.url)
        item['themeDomain'] = theme
    
        onSale = response.xpath('/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/section/div[2]/div[2]/div[1]/div[2]/text()').extract_first() # |//div[@class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount"]/text()
        avgSale = response.xpath('/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/text()').extract_first() # |//div[@class="PriceHistoryStats--value"]/text()
        avgSale = avgSale[1:] if avgSale is not None else None
        item["onSalePrice"] = onSale if onSale is not None  else avgSale

        tradingEvent = response.xpath('/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div')
        lastPrice = ''
        for tradeitem in tradingEvent:
            if "Sale" == tradeitem.xpath('./div[1]/span/text()').extract_first(): 
                lastPrice = tradeitem.xpath('./div[2]/div/div/div[2]/text()').extract_first()
                break
        
        item["dealPrice"] = lastPrice if  lastPrice!= '' else "not know"
        
        properties = response.xpath('/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[1]/section/div/div[2]/div/div/div/div/a/div/div[3]/text()').extract()
        propertiesList = []
        [ propertiesList.append(float(rate.split("%")[0])) for rate in properties  ]
        item["rareness"] = math.prod(propertiesList)
        
        yield item

    def errback_httpbin(self,failure):
        """
        HttpErrHandle callback function
        """
        # log all failures
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on url: %s, reason: %s', response.url, response.text)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
    