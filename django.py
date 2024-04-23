from django.conf import settings

from settings.config import Config

#
# WebCrawler filtered domains
#
WEBCRAWLER_FILTERED_DOMAINS = Config.list('ZIMAGI_WEBCRAWLER_FILTERED_DOMAINS', [
    'google.com',
    'bing.com',
    'perplexity.ai',
    'you.com',
    'yep.com',
    'openverse.org',
    'yahoo.com',
    'aol.com',
    'duckduckgo.com',
    'startpage.com',
    'brave.com',
    'wiki.com',
    'wikipedia.com',
    'x.com',
    'twitter.com',
    'facebook.com',
    'instagram.com',
    'slideshare.net',
    'linkedin.com'
])
