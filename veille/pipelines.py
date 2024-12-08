# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



class VeillePipeline:
    def process_item(self, item, spider):
        return item


class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('ai_tools.db')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO ai_tools (category, title, description, tags, link, type, final_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            item.get('category'),
            item.get('title'),
            item.get('description'),
            '|'.join(item.get('tags', [])),  # Transforme la liste en chaîne
            item.get('link'),
            item.get('type'),
            None,
        ))
        return item
