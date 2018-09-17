# -*- coding: utf-8 -*-
import scrapy
from douban_movie.items import DoubanMovieItem
# 爬取豆瓣电影前250的电影信息
class DoubanmoviesSpider(scrapy.Spider):
    name = 'doubanMovies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        movie_list = response.xpath('//ol[@class="grid_view"]//li')
        for movie in movie_list:
            item = DoubanMovieItem()
            item['movie_pic'] = movie.xpath('.//div[@class="item"]//div[@class="pic"]//img/@src').extract_first()
            item['movie_title'] = movie.xpath('.//div[@class="item"]//div[@class="hd"]//a//span[@class="title"]/text()').extract_first()

            span2 = movie.xpath('.//div[@class="item"]//div[@class="hd"]//a//span[2]/text()').extract_first()
            span3 = movie.xpath('.//div[@class="item"]//div[@class="hd"]//a//span[3]/text()').extract_first()
            item['movie_other'] = ((span2 if span2 else '') + (span3 if span3 else '')).replace(u'\xa0', u' ')

            item['movie_introduce'] = movie.xpath('normalize-space(.//div[@class="item"]//div[@class="bd"]//p[1]/text())').extract_first().replace(u'\xa0', u' ')
            item['movie_star'] = movie.xpath('.//div[@class="bd"]//div[@class="star"]/span[2]/text()').extract_first()
            item['evaluate_num'] = movie.xpath('.//div[@class="bd"]//div[@class="star"]/span[4]/text()').extract_first()
            item['movie_description'] = movie.xpath('.//div[@class="bd"]//p[@class="quote"]/span/text()').extract_first()

            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            print(self.start_urls[0] + next_url)
            yield scrapy.Request(self.start_urls[0]+next_url, callback=self.parse)

