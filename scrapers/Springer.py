from logic.System import System
from scrapers.Scraper import Scraper


class Springer(Scraper):

    __piiArray = []
    __rawArray = []

    def __init__(self, piiArray):
        super(Springer, self).__init__()
        self.TYPE = System.CrawlerType.SPRINGER
        self.__piiArray = piiArray

    def get(self):
        pass

    def run(self):
        pass
