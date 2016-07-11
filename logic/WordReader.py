import os
from zipfile import ZipFile

from bs4 import BeautifulSoup


class WordReader(ZipFile):

    __list = []
    __count = 0
    __xmlDict = None
    __xmlClass = None
    __xmlContent = None

    def __init__(self, fileName, path=None):
        self.__changeDir(path)
        super(WordReader, self).__init__(fileName, "r")
        self.__initTags()
        self.__readXml()
        self.__parseXml()

    def __initTags(self):
        if self.getFormat(self.filename).lower() == "docx":
            self.__xmlContent = "word/document.xml"
            self.__xmlClass = "w:t"
            self.__xmlDict = {"xml:space": "preserve"}
        elif self.getFormat(self.filename).lower() == "odt":
            self.__xmlContent = "content.xml"
            self.__xmlClass = "text:a"
            self.__xmlDict = {"xlink:type": "simple"}
        else:
            raise RuntimeError("__readXml(): file format not supported.")

    def __readXml(self):
        self.__xml = self.read(self.__xmlContent)
        self.close()

    def __parseXml(self):
        root = BeautifulSoup(self.__xml, "lxml")
        for child in root.findAll(self.__xmlClass, self.__xmlDict):
            href = child.string
            if href[0] == "<" and href[len(href)-1] == ">":
                self.__list.append(href[1:len(href)-1])

    @staticmethod
    def getFormat(filename):
        return os.path.splitext(filename)[1][1:]

    @staticmethod
    def __changeDir(path):
        if path is not None:
            os.chdir(path)

    def get(self):
        return self.__list
