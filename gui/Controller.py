# -*- coding: utf-8 -*-
import os
import sys

from PyQt4.Qt import *

from gui.AboutView import AboutView
from gui.ImportFileView import ImportFileView
from gui.MainStage import MainStage
from gui.TabView import TabView
from logic.System import System
from logic.WordReader import WordReader
from logic.Wrnings import Warnings


class Controller(System):

    __window = None
    __rightWindow = None

    def __init__(self):
        super(Controller, self).__init__()
        self.__window = MainStage(self)
        self.__rightWindow = self.__window.vBox
        self.__window.show()
        self.__showAbout()

    def __showImportFileView(self):
        linksView = ImportFileView(self, self.__rightWindow)

    def __showTabView(self):
        tabView = TabView(self, self.__rightWindow, "Domains")
        tabView.addItems("Domains", self.getAllAvailableDomains(), QCheckBox)

    def __showAbout(self):
        aboutView = AboutView(self.__rightWindow)
        aboutView.initView()

    def __initNullScene(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                if hasattr(item, "count"):
                    self.__initNullScene(item.layout())

    def updateLinks(self, fileName, filePath):
        if fileName is not None:
            fileType = WordReader.getFormat(fileName).lower()
            if fileType == "odt" or fileType == "docx":
                self.extractLinks(fileName, filePath)
            else:
                self.showWarning(Warnings.fileTypeException())
        else:
            self.showWarning(Warnings.noneFileException())

    def update(self, treeItem, idx):
        self.__initNullScene(self.__rightWindow)
        if treeItem.text(idx) == "Import file":
            self.__showImportFileView()
            self.__window.statusLabel.setText(treeItem.text(idx))
        elif treeItem.text(idx) == "Options":
            self.__showTabView()
            self.__window.statusLabel.setText(treeItem.text(idx))
        elif treeItem.text(idx) == "About":
            self.__showAbout()
            self.__window.statusLabel.setText(treeItem.text(idx))
        else:
            self.__window.statusLabel.setText(treeItem.text(idx))

    @staticmethod
    def showWarning(msg):
        wBox = QMessageBox()
        wBox.setIcon(QMessageBox.Warning)
        wBox.setWindowTitle("Warning")
        wBox.setText(msg)
        wBox.setStandardButtons(QMessageBox.Ok)
        wBox.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    controller = Controller()
    app.exec_()

