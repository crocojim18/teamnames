# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CountnounsPipeline:
    def process_item(self, item, spider):
        return item

class TxtExportPipeline:
	def __init__(self):
		self.file = None

	def open_spider(self, spider):
		self.file = open("output.txt", 'wb')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		for i in item["out"]:
			self.file.write("{}\n".format(i).encode('utf8'))
		return item

