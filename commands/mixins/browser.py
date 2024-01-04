from systems.commands.index import CommandMixin
from utility.data import Collection
from bs4 import BeautifulSoup


class BrowserCommandMixin(CommandMixin('browser')):

    def parse_webpage(self, url):
        webpage = self.submit('agent:browser', url)
        return Collection(
            url = webpage['url'],
            soup = BeautifulSoup(webpage['source'], 'html.parser')
        )
