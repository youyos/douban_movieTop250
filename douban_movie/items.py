# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影标题
    movie_title = scrapy.Field()

    # 其他
    movie_other = scrapy.Field()

    # 电影描述
    movie_introduce = scrapy.Field()

    # 电影星级
    movie_star = scrapy.Field()

    # 评价人数
    evaluate_num = scrapy.Field()

    # 电影描述
    movie_description = scrapy.Field()

    # 封面图
    movie_pic = scrapy.Field()



