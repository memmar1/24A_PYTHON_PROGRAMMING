class BeutifulSoup()
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.soup.prettify()