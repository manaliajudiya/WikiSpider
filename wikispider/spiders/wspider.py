from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wikispider.items import WikispiderItem
from scrapy.selector import HtmlXPathSelector

class WspiderSpider(CrawlSpider):
    name = 'wspider'
    allowed_domains = ['wikipedia.org']
    start_urls = ["http://en.wikipedia.org/wiki/Mathematics"]

    rules=(
    
    Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="mw-body"]//a/@href'))),
    Rule(SgmlLinkExtractor(allow = ("http://en.wikipedia.org/wiki/")),callback='parse_item'),

    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//h1[@class='firstHeading']")        
        items = []
        for site in sites:
            item = WikispiderItem()
            item['title'] = site.select('span/text()').extract()
            items.append(item)
        return items
       
