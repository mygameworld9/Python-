from scrapy import cmdline
cmdline.execute("Scrapy crawl mySpider -s LOG_ENABLED=False".split())
