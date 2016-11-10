# encoding=utf-8
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl Spider1'.split())
    # cmdline.execute('scrapy crawl Spider2'.split())
