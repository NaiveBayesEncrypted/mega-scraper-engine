import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RentFasterSpider(CrawlSpider):
    """
    NEXUS PORTFOLIO PROJECT: Calgary Real Estate Intelligence
    Goal: Identify undervalued rental properties in Calgary using RentFaster.ca
    Status: BUILD ONLY (Do not execute without proxy rotation)
    """
    name = 'rent_faster_spider'
    allowed_domains = ['rentfaster.ca']
    start_urls = ['https://www.rentfaster.ca/ab/calgary/']

    # Professional Rule set for navigating rental listings
    rules = (
        Rule(LinkExtractor(allow=('/ab/calgary/rentals/', )), callback='parse_listing'),
    )

    def parse_listing(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'price': response.css('.price::text').get(),
            'neighborhood': response.css('.community::text').get(),
            'sq_ft': response.css('.sq-ft::text').get(),
            'url': response.url,
            'scraped_at': response.xpath('now()').get()
        }

# NEXUS NOTE: This is a high-value portfolio project for the Calgary market. 
# It showcases expertise in Scrapy, LinkExtractors, and local market analysis.
