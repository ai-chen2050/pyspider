# Scrapy settings for opensea project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import logging

BOT_NAME = 'opensea'

SPIDER_MODULES = ['opensea.spiders']
NEWSPIDER_MODULE = 'opensea.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'opensea (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 日志等级
LOG_LEVEL = logging.INFO

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'opensea.middlewares.OpenseaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'opensea.middlewares.UserAgentMiddleware': 540,
   'opensea.middlewares.OpenseaDownloaderMiddleware': 543,
   'aroay_cloudscraper.downloadermiddlewares.CloudScraperMiddleware': 560,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'opensea.pipelines.OpenseaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

"""
aroay cloudscarper setting
"""
# 默认日志级别
AROAY_CLOUDSCRAPER_LOGGING_LEVEL = logging.INFO

#默认超时
AROAY_CLOUDSCRAPER_DOWNLOAD_TIMEOUT = 30

# 默认延迟
AROAY_CLOUDSCRAPER_DELAY = 1

#必须设置，否则报错
COMPRESSION_ENABLED = False

RETRY_ENABLED: True
RETRY_TIMES: 3

"""
selenium
"""
# ----------- selenium 参数配置 -------------
SELENIUM_TIMEOUT = 25           # selenium 浏览器的超时时间，单位秒
LOAD_IMAGE = False               # 是否下载图片
WINDOW_HEIGHT = 900             # 浏览器窗口大小
WINDOW_WIDTH = 900


"""
The Business Config Field
"""

class selfConfig(object):
   # 保守估计迭代一次大约 12 个 NFT 页面。实际得到的数量可能会大约 20 * 12。实测迭代 20 轮 425 条页面数据
   # 爬取策略为模拟手工操作点击，一个页面约 3s 上下
   ITERATOR_ROUND_NUM = 20 

   # 关键词列表支持多个同时搜索，数据根据关键词命名保存为 JSON 格式, 
   # 若需保存到数据库。如 MongoDB or MySQL 需要另行开发

   SEARCH_THEME_WORDS = ["cryptopunks"]
   
