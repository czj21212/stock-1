# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TonghuashunPipeline(object):
    def process_item(self, item, spider):
        number = item["number"]
        stock_num = item["stock_num"]
        stock_name = item["stock_name"]
        now_price = item["now_price"]
        puls_price = item["puls_price"]
        deal_num = item["deal_num"]
        print("序号：{} 股票代码：{} 股票名称：{} 现价：{} 涨幅：{} 成交额：{}".format(number,stock_num,stock_name,now_price,puls_price,deal_num))
        return item
