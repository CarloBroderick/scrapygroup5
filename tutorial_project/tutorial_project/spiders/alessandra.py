import scrapy


class AlessandraSpider(scrapy.Spider):
    name = 'alessandra'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        rows = response.xpath('//tr')
        # print(rows)

        for row in rows:
            # title =  response.xpath('//h1/text()').get()
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()
            # print(countries)
            # print(population)
        
            yield {
                'countries': countries,
                'population': population,
            }
