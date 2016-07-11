from logic.WordReader import WordReader
from urlparse import urlparse


class System(object):

    __links = []
    __scrapers = []
    __linkCount = 0
    __linksByDomain = {}

    class CrawlerType(enumerate):
        SCIENCEDIRECT = 1
        SPRINGER = 2

    def extractLinks(self, fileName, path):
        reader = WordReader(fileName, path)
        self.__links = reader.get()
        self.__linkCount = len(self.__links)
        self.__constructLinksByDomain()

    def initScrapers(self): pass

    def runCrawl(self): pass

    def getAllAvailableDomains(self):
        return ["sciencedirect.com", "springer.com", "chf.vu.lt"]

    def getPagesDomains(self):
        return self.__linksByDomain.keys()

    def getLinksByDomain(self):
        return self.__linksByDomain

    def getCount(self):
        return self.__linkCount

    def getLinks(self):
        return self.__links

    def __constructLinksByDomain(self):
        for link in self.__links:
            domain = urlparse(link)[1]
            if domain not in self.__linksByDomain.keys():
                self.__linksByDomain[domain] = [link]
            else:
                self.__linksByDomain[domain].append(link)
