# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from selenium import webdriver
from scrapy.http import HtmlResponse
import time


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url
        if 'herolist' in url or 'herodetail' in url:
            # 设置Edge无头浏览器模式
            EDGE = {
                "browserName": "MicrosoftEdge",
                "version": "100.0.1185.44",
                "platform": "WINDOWS",
                "ms:edgeOptions": {
                    'extensions': [],
                    'args': [
                        '--headless',
                        '--disable-gpu'
                    ]}
            }
            web = webdriver.Edge(capabilities=EDGE)
            web.get(url)
            time.sleep(1)
            # 返回浏览器渲染后的页面
            data = web.page_source
            web.close()
            # 创建响应对象
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            return res
