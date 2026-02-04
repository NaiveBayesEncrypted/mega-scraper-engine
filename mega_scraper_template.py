import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CompetitorSpyder(CrawlSpider):
    name = 'competitor_spyder'
    allowed_domains = ['example-retail.ca'] # We will parameterize this
    start_urls = ['https://example-retail.ca/collections/all']

    rules = (
        Rule(LinkExtractor(allow=('/products/', )), callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'name': response.css('h1.product-title::text').get(),
            'price': response.css('.price-item--regular::text').get(),
            'sku': response.css('.variant-sku::text').get(),
            'url': response.url,
            'timestamp': response.xpath('now()').get()
        }

# NEXUS NOTE: This is the structure of the mega-scraper you built. 
# We will use this to showcase your ability to handle 20k+ links.
