# encoding=utf-8
# ---------------------------------------
#   版本：0.1
#   日期：2016-11-10
#   作者：九茶<bone_ace@163.com>
# ---------------------------------------

from scrapyWithBloomfilter_demo.scrapy_redis.spiders import RedisSpider
from scrapy.http import Request


class Spider1(RedisSpider):
    name = "Spider1"
    redis_key = "scrapyWithBloomfilter_demo:start_urls"
    start_urls = [
        'http://tieba.baidu.com/p/4855113094?pn=1',
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=3',
        'http://tieba.baidu.com/p/4855113094?pn=4',

        'http://tieba.baidu.com/p/4855113094?pn=2',  # 这四个URL已爬，将被去重
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=3',

        'http://tieba.baidu.com/p/4855113094?pn=5',
        'http://tieba.baidu.com/p/4855113094?pn=6',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse1)

    def parse1(self, response):
        print 'We Get: %s' % response.url


class Spider2(RedisSpider):
    name = "Spider2"
    redis_key = "scrapyWithBloomfilter_demo:start_urls"
    start_urls = [
        'http://tieba.baidu.com/p/4855113094?pn=1',
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=3',
        'http://tieba.baidu.com/p/4855113094?pn=4',

        'http://tieba.baidu.com/p/4855113094?pn=2',  # 这四个URL已爬，将被去重
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=2',
        'http://tieba.baidu.com/p/4855113094?pn=3',

        'http://tieba.baidu.com/p/4855113094?pn=5',
        'http://tieba.baidu.com/p/4855113094?pn=6',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse1)

    def parse1(self, response):
        print 'We Get: %s' % response.url
