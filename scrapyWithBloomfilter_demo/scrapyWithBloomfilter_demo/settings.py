# encoding=utf-8
# ---------------------------------------
#   版本：0.1
#   日期：2016-11-10
#   作者：九茶<bone_ace@163.com>
# ---------------------------------------


BOT_NAME = 'scrapyWithBloomfilter_demo'
SPIDER_MODULES = ['scrapyWithBloomfilter_demo.spiders']
NEWSPIDER_MODULE = 'scrapyWithBloomfilter_demo.spiders'

SCHEDULER = 'scrapyWithBloomfilter_demo.scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapyWithBloomfilter_demo.scrapy_redis.queue.SpiderPriorityQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapyWithBloomfilter_demo.scrapy_redis.queue.SpiderSimpleQueue'

# 种子队列的信息
REDIE_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0
# REDIS_QUEUE_NAME = 'OneName'   # 如果不设置或者设置为None，则使用默认的，每个spider使用不同的去重队列和种子队列。如果设置了，则不同spider共用去重队列和种子队列


LOG_LEVEL = 'INFO'
CONCURRENT_REQUESTS = 1  # 并发
