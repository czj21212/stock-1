# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import TonghuashunItem


class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ['10jqka.com.cn']
    # 通过查看响应能知道同花顺的数据是通过ajax生成的 找到真正的地址 这个地址是根据整个页面刷新可得
    start_urls = ['http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/']
    page = 1

    def parse(self, response):
        tr_list = response.xpath('//tbody/tr')
        page_num = response.xpath('//*[@id="m-page"]/span/text()').extract()[0]
        page_num = re.findall(r"\d+/(\d+)", page_num)[0]
        for tr in tr_list:
            item = TonghuashunItem()
            item["number"] = tr.xpath('./td[1]/text()').extract_first()
            item["stock_num"] = tr.xpath('./td[2]/a/text()').extract_first()
            item["stock_name"] = tr.xpath('./td[3]/a/text()').extract_first()
            item["now_price"] = tr.xpath('./td[4]/text()').extract_first()
            item["puls_price"] = tr.xpath('./td[5]/text()').extract_first()
            item["deal_num"] = tr.xpath('./td[11]/text()').extract_first()
            yield item
        if self.page <= int(page_num):
            self.page += 1
            next_url = "http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/".format(self.page)

            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )
