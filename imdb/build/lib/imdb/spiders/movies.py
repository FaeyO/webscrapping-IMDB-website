import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = "movies"
    allowed_domains = ["web.archive.org"]
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url="https://web.archive.org/web/20200715000935/https://www.imdb.com/search/title/?groups=top_250",headers={'user_agent':self.user_agent})

    rules = (Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback="parse_item", follow=True, process_request='set_user_agent'),
             Rule(LinkExtractor(restrict_xpaths="(//div[@class='desc'])[2]/a"))
             )
    
    def set_user_agent(self,request,spider):
        request.headers['User_Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'title' : response.xpath("(//div[@class='title_wrapper']/h1/text())[1]").get(),
            'year' : response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration' : response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'movie_link' : response.url,
            'genre' : response.xpath("//div[@class='subtext']/a/text()").get(),
            'rating' : response.xpath("//div[@class='ratingValue']/strong/span/text()").get()
        }
