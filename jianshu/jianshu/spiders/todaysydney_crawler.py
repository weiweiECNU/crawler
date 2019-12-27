from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from jianshu.items import JianshuItem
import re

class today_sydney(CrawlSpider):
    name = 'today_sydney'
    start_url = 'https://www.sydneytoday.com/house_rent/191950570193058'

    def parse(self, response):
        """
            response 是请求网页返回的数据
        """
        item = JianshuItem()
        selector = Selector(response)

        title = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/h1/text()').extract()[0]
        time = re.findall(r'\d{4}-\d{2}-\d{2}', selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/span[1]/text()').extract()[0])[0]
        price = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/text()').extract()[0]
        style = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/text()').extract()[0][4:]
        source = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/text()').extract()[0][4:]
        house_type = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/text()').extract()[0][4:]
        devices = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/text()').extract()[0][4:]
        address = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div[6]/text()').extract()[0][4:]
        description = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[4]/text()').extract()[0]

        item['title'] = title
        item['time'] = time
        item['rent'] = price
        item['rent_style'] = style
        item['source'] = source
        item['type'] = house_type
        item['devices'] = devices
        item['address'] = address
        item['text'] = description

        yield item



