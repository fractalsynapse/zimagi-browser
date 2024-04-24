from django.conf import settings

from settings.config import Config

#
# WebCrawler filtered domains
#
WEBCRAWLER_FILTERED_DOMAINS = Config.list('ZIMAGI_WEBCRAWLER_FILTERED_DOMAINS', [])
