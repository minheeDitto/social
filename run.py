#-*- coding:utf-8 -*-
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from ins.spiders.fb_fans import FbFansSpider



settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(FbFansSpider)
process.start()
process.join()