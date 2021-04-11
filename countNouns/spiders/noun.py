import scrapy, re


class noun(scrapy.Spider):
	name = "noun"

	def start_requests(self):
		urls = [
			'https://en.wiktionary.org/wiki/Category:en:Places_in_the_United_States'#,
			#'https://en.wiktionary.org/wiki/Category:English_noun_forms'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		if response.xpath('//a[contains(text(), "next page")]')!=None:
			newlink = response.urljoin(response.xpath('//a[contains(text(), "next page")]/@href').get())
			yield scrapy.Request(url=newlink, callback=self.parse)
		yield {"out": response.xpath('//div[@class="mw-category-group"]//li/a/text()').getall()}
