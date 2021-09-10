# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AtualizafolhaspPipeline:
    def process_item(self, item, spider):
        data = item['link'].split('/')

        item['category']    = data[3]
        if not data[4].isdigit():
          item['subcategory'] = data[4]

        return item


class CleanData(object):
    # Remove \t\r\n
    def process_item(self, item, spider):
        for field in ['text', 'created_at']:
          item[field] = item[field].replace('\t', ' ')
          item[field] = item[field].replace('\r', ' ')
          item[field] = item[field].replace('\n', ' ')
          item[field] = item[field].strip()
          
        return item
