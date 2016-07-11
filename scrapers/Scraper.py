from abc import ABCMeta, abstractmethod
from threading import Thread


class Scraper(Thread):
    __metaclass__ = ABCMeta
    TYPE = None

    @abstractmethod
    def get(self): pass

    @abstractmethod
    def run(self): pass

