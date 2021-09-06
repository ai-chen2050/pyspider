# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json, os
# from settings import SEARCH_THEME_WORDS
from opensea.settings import selfConfig

SEARCH_THEME_WORDS = selfConfig.SEARCH_THEME_WORDS

class OpenseaPipeline:
    def __init__(self):
        self.Domainum = len(SEARCH_THEME_WORDS)
        self.storeByDomain = {}
        for item in SEARCH_THEME_WORDS:
            self.storeByDomain[item] = self.makeFileHandler(item)
            self.storeByDomain[item][0].write(bytes("{\n ", encoding='utf-8'))
    
    def process_item(self, item, spider):
        self.storeByDomain[item["themeDomain"]][1].append(item)
        return item
    
    def close_spider(self, spider):
        
        for keyword in SEARCH_THEME_WORDS:
            file_handler = self.storeByDomain[keyword][0]
            sorted_list = self.storeByDomain[keyword][1]
            sorted_list = sorted(sorted_list, key=lambda x: x['rareness'])
            
            for nft_item in sorted_list:
                content = "\"" + nft_item["themeDomain"] + "-" + nft_item["ntfUrl"].split("/")[-1] + "\"" + ": " +json.dumps(dict(nft_item), ensure_ascii = False) + ',\n'
                file_handler.write(bytes(content, encoding='utf-8'))
            file_handler.seek(-2, 2 )
            file_handler.truncate()
            file_handler.write(bytes("\n }", encoding='utf-8'))
            file_handler.close()

    def makeFileHandler(self, filename):
        return  [ open(filename + ".json", "wb"), [] ]
            
        
