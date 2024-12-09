# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



class AiToolsPipeline:
    def process_item(self, item, spider):
        self.conn = spider.conn
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            INSERT INTO ai_tools (category, title, description, type, inner_url, outer_url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item.get('category'),
            item.get('title'),
            item.get('description'),
            item.get('type'),
            item.get('inner_url'),
            item.get('outer_url'),
        ))

        return item


class TagsPipeline:
    def process_item(self, item, spider):
        self.conn = spider.conn
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            UPDATE ai_tools_concat
               SET tags = ?
             WHERE id = ?
        ''', (
            item.get('tags'),
            item.get('id'),
        ))

        return item