from scrapy.cmdline import execute
from settings import selfConfig
import sys
import os


def startCrawling(iterNum=None, keywords=None):
    # 获取当前脚本路径
    dirpath = os.path.dirname(os.path.abspath(__file__))
    print(dirpath)
    # 添加环境变量
    sys.path.append(dirpath)

    if iterNum != None:
        selfConfig.ITERATOR_ROUND_NUM = iterNum
        selfConfig.SEARCH_THEME_WORDS = keywords
    
    # 启动爬虫,第三个参数为爬虫name
    execute(['scrapy','crawl','opensee']) #, "-o","news.csv", "-t", "csv" ,'-s','LOG_FILE=all.log'])


# startCrawling()
