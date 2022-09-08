import scrapy


class CarloSpiderSpider(scrapy.Spider):
    name = 'carlo_spider'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        rows = response.xpath('//tr')
        
        for row in rows:
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()
            density = row.xpath('./td[6]/text()').get()
            fert_rate = row.xpath('./td[9]/text()').get()
            med_age = row.xpath('./td[10]/text()').get()
            
            yield {
                'countries' : countries,
                'population' : population,
                'density' : density,
                'fert_rate' : fert_rate,
                'med_age' : med_age
            }
