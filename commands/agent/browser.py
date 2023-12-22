from systems.commands.index import Agent
from utility.browser import Browser as WebBrowser


class Browser(Agent('browser')):

    def exec(self):
        channel = 'agent:browser'

        for package in self.listen(channel, state_key = 'browser'):
            url = package.message

            try:
                self.data('Processing browser request', package.sender)
                response = self.profile(self._fetch_html, url)
                self.send(package.sender, response.result)

            except Exception as e:
                self.send(channel, package.message, package.sender)
                raise e

            self.send("{}:stats".format(channel), {
                'url': url,
                'html_length': len(response.result),
                'time': response.time,
                'memory': response.memory
            })

    def _fetch_html(self, url):
        return WebBrowser(url).source
