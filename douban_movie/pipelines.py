# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class DoubanMoviePipeline(object):

    def __init__(self):
        mongo_host = 'localhost'
        mongo_port = 27017
        mongo_database = 'test'
        mongo_collection = 'movie_top250'

        client = pymongo.MongoClient(mongo_host, mongo_port)

        db = client[mongo_database]

        self.collection = db.get_collection(mongo_collection)




    def process_item(self, item, spider):
        # collection
        self.collection.insert_one(dict(item))
        return item
