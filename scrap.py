import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://guitarpatches.com/patches.php?unit=G3']

    def parse(self, response):
        for table_row in response.css('.lists tbody')[0].css('tr'):
            yield self.extract_tuple(table_row)

        for next_page in response.xpath('//a[contains(text(), "next")]'):
            yield response.follow(next_page, self.parse)

    def extract_tuple(self, row):
        columns = row.css('td')
        link = row.css('a')
        
        link_href = link.css('a::attr(href)').extract_first()
        column = lambda index, selector = 'p::text': columns[index].css(selector).extract_first()
        
        rating = column(2, 'b::text')
        return {
            'link': link_href,
            'index': link_href.split('=')[-1],
            
            'title': link.css('a::text').extract_first(),
            'artist': column(1).strip(),
            'rating': None if rating is None else float(rating),
            'has_audio': column(3, 'img') is not None,
            'has_video': column(4, 'img') is not None,
            'date': column(5).strip(),
            'uploader': column(6).strip(),
            'total_downloads': int(column(7)),
        }

# Rodar na versão mais nova
#scrapy runspider scrap.py -o data/pedalboard-info.json
'''
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data/pedalboard-info.json',
})


process.crawl(BlogSpider)
process.start()
process.stop()
'''