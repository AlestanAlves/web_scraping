import scrapy 
from bz2 import open

class cnpj(scrapy.Spider):
    name = "cnpjCrawl"

    def start_requests(self):
        urls = [
            "https://cnpj.biz/33513337000151"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            filename = "test.html"

            with open(filename,'wb') as f:
                f.write(response.body)