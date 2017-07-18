import scrapy

from weather.items import WeatherItem


class weatherSpider(scrapy.spiders.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@class="even"]'):
            name = sel.xpath('./td[1]/a/test()').extract()[0]
            print (name)

            item = WeatherItem()
            item.name = name.encode('utf-8')

            yield item