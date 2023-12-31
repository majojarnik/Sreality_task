import scrapy
import json
from sreality.sreality.items import SrealityItem


class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response, **kwargs):
        dict_response = json.loads(response.text)
        for flat in dict_response.get('_embedded').get('estates'):
            item = SrealityItem()
            item['title'] = flat['name']
            item['image_url'] = flat['_links']['image_middle2'][0]['href']

            yield item


