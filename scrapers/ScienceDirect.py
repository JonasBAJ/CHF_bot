from logic.System import System
from scrapers.Scraper import Scraper
import requests


class ScienceDirect(Scraper):

    __piiArray = []
    __rawArray = []
    __headers = {
        "Accept": "application/xml",
        "Content-Type": "application/json",
        "APIKey": "6492f9c867ddf3e84baa10b5971e3e3d"
    }

    def __init__(self, piiArray):
        super(ScienceDirect, self).__init__()
        self.TYPE = System.CrawlerType.SCIENCEDIRECT
        self.__piiArray = piiArray

    def getRawInfo(self):
        for pii in self.__piiArray:
            req = requests.get(
                "http://api.elsevier.com:80/content/article/pii/" + pii + "?apiKey=6492f9c867ddf3e84baa10b5971e3e3d",
                params=self.__headers
            )
            self.__rawArray.append(req.text)

    def extractInfo(self):
        pass

    def get(self):
        pass

    def run(self):
        pass
