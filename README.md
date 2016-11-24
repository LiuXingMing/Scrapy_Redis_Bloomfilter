##bloomfilterOnRedis.py：##
基于Redis的Bloomfilter去重，已经封装成一个类，只需两行代码即可实现去重。更多介绍见：[《基于Redis的Bloomfilter去重（附Python代码）》](http://blog.csdn.net/bone_ace/article/details/53107018)。

</br></br>
##scrapyWithBloomfilter_demo：##
一个简单的scrapy demo，对scrapy_redis模块作了一些修改，将去重模块替换成了Bloomfilter去重。更多介绍见：[《scrapy_redis去重优化（已有7亿条数据），附Demo福利》](http://blog.csdn.net/bone_ace/article/details/53099042)。

</br></br>
##种子优化：##
在scrapyWithBloomfilter_demo中我对默认的种子作了一些修改，在settings.py中将 SCHEDULER_QUEUE_CLASS 改成 'scrapyWithBloomfilter_demo.scrapy_redis.queue.SpiderSimpleQueue' 即可。详细介绍见：[《scrapy_redis种子优化》](http://blog.csdn.net/bone_ace/article/details/53306629)。
</br></br>
