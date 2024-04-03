from systems.commands.index import CommandMixin
from utility.data import Collection
from bs4 import BeautifulSoup

import re


class BrowserCommandMixin(CommandMixin('browser')):

    def parse_webpage(self, url):
        webpage = self.submit('agent:browser', url)
        soup = BeautifulSoup(webpage['source'], 'html.parser')
        text = ''

        if webpage['source']:
            text = re.sub(r'\n+', '\n', soup.get_text("\n")).encode('ascii', errors = 'ignore').decode().strip()

        return Collection(
            url = webpage['url'],
            text = text,
            soup = soup
        )
