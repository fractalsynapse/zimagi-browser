from systems.commands.index import CommandMixin
from utility.data import Collection
from utility.web import WebParser
from bs4 import BeautifulSoup

import re


class BrowserCommandMixin(CommandMixin('browser')):

    def parse_webpage(self, url):
        webpage = self.submit('agent:browser', url, timeout = 30)
        browser = None
        text = ''

        if webpage['source']:
            soup, text = self._parse_webpage_text(webpage['source'])
        if not text:
            browser = WebParser(url, verify = False)
            soup, text = self._parse_webpage_text(browser.text)

        return Collection(
            url = webpage['url'] if not browser else url,
            title = soup.title.text.encode('ascii', errors = 'ignore').decode().strip() if soup.title else '',
            text = text,
            soup = soup
        )

    def _parse_webpage_text(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        text = re.sub(r'\n+', '\n', soup.get_text("\n")).encode('ascii', errors = 'ignore').decode().strip()
        return soup, text
