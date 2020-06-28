# -*- coding: utf-8 -*-
import scrapy
import pickle
import json
from scrapy.utils.reqser import request_from_dict


class RabbitSpider(scrapy.Spider):
    def _make_request(self, mframe, hframe, body):
        try:
            request = request_from_dict(json.loads(body), self) # json 数据
        except Exception:
            body = body.decode()
            data = json.loads(body,encoding="utf-8")
            request = scrapy.Request(data['url'], callback=self.parse, dont_filter=True,meta=data['params'])
        return request
