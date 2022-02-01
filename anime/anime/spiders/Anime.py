import scrapy

class animecrawler(scrapy.Spider):
    name = 'anime'

    start_urls = [
        'https://myanimelist.net/anime/season'
    ]

    def parse(self, response):
        for post in response.css('div.title'):
            yield{
                'title' : post.css('.title-text h2.h2_anime_title a.link-title::text').get()
            }
        for post in response.css('div.info'):
            yield{
                'lancamento' : post.css('span.item::text')[0].get()
            }