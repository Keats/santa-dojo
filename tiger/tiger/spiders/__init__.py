import scrapy

from .. import items


class BlogSpider(scrapy.Spider):
    name = 'tiger'
    allowed_domains = ["www.tigerstores.co.uk"]
    start_urls = ['http://www.tigerstores.co.uk/']

    def parse(self, response):
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)

        name = response.xpath('//h1/text()').extract_first()
        pic = response.xpath('//div[@class="cc"]//img/@src').extract_first()
        price =  response.xpath('//div[@class="priceAddToBasket"]/span/text()').extract_first()


        yield items.TigerItem(
            name=name,
            pic=pic,
            price=price
        )
