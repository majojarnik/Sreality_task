from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from sreality.sreality import settings as my_settings
from sreality.sreality.spiders.flats import FlatsSpider


class Command(BaseCommand):
    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(FlatsSpider)
        process.start()
