from systems.commands.index import Command


class Browser(Command('browser')):

  def exec(self):
    self.data('HTML Webpage',
        self.submit('agent:browser', self.url),
        'webpage_html'
    )
